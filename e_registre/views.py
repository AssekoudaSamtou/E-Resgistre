from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib import messages
from django.http import HttpResponse, Http404

from .forms import EtudiantForm, VisiteForm, VisiteurForm, EnseignantForm, PersonnelForm
from .models import Etudiant, Visiteur, Enseignant, Personnel, Visite
import datetime

categories = {"etudiant"  : Etudiant, 
			  "autre"     : Visiteur, 
			  "enseignant": Enseignant, 
			  "personnel" : Personnel}

motifs = {"etudiant"  : "Cours", 
		  "autre"     : "Visiteur", 
		  "enseignant": "Enseignant", 
		  "personnel" : "Personnel"}

def add_personne(request, categorie):
	print(categorie)
	categories = {"etudiant" : EtudiantForm, "autre": VisiteurForm, "enseignant": EnseignantForm, "personnel": PersonnelForm}
	if request.method ==  'POST':
		f = categories[categorie](request.POST)
		if f.is_valid():
			personne = f.save()
			return redirect(reverse('e_registre:liste', args=[categorie]))

	else:
		f = categories[categorie]()
	return render(request, 'e_registre/ajout_personne.html', {'form': f})

def liste(request, categorie):
	personnes = categories[categorie].objects.all()
	return render(request, 'e_registre/liste.html', {'personnes': personnes, 'cate': categorie})

def detail(request, categorie, id):
	personne = get_object_or_404(categories.get(categorie), id=id)
	visites = Visite.objects.filter(visiteur=personne)
	# personne.save()
	return render(request, 'e_registre/detail.html', {'visites': visites, "visiteur": personne})

def home(request):
	if request.method == "GET":
		categorie = request.GET.get("categorie")
		nom = request.GET.get("name")
		if categorie == None:
			categorie = "etudiant"
		if nom == None:
			
			personnes = categories[categorie].objects.all()
			print(personnes)
		else:
			personnes = categories[categorie].objects.filter(nom__contains=nom)
		visites = {}
		for p in personnes:
			visites_de_p = Visite.objects.filter(visiteur=p).order_by("-date_de_visite")
			if len(visites_de_p) == 0:
				visites[p] = ("", "")
			else:
				visites[p] = (visites_de_p[0].heure_darrive, visites_de_p[0].heure_depart)
		print(visites)
	if visites == {} : visites = { p : ("", "") for p in personnes }
	contexte = {"personnes" : visites, 'cate': categorie}
	if request.is_ajax():
		return render(request, 'layout/ajax_home.html', contexte)
	return render(request, 'e_registre/home.html', contexte)

def date_is(request):
	now = datetime.datetime.now()
	now = now.strftime("%Y %M %d %H-%M-%S")
	return render(request, 'e_registre/now.html', locals())

def debut_visite(request, categorie, id):
	if request.is_ajax():
		visiteur = get_object_or_404(categories.get(categorie), id=id)
		visite = Visite(visiteur=visiteur, motif=motifs[categorie])
		visite.save()
		now = visite.heure_darrive.now()
		print(now.strftime("%HH %Mm %Ss"))
		return HttpResponse(f"{now.strftime('%H:%M:%S')}")

def fin_visite(request, categorie, id):
	if request.is_ajax():
		visiteur = get_object_or_404(categories.get(categorie), id=id)
		visite = Visite.objects.filter(visiteur=visiteur).order_by("-date_de_visite")[0]
		visite.heure_depart = datetime.datetime.now()
		visite.save()
		print(visite)
		return HttpResponse(f"{visite.heure_depart.now().strftime('%H:%M:%S')}")
