from django import forms
from django.core.exceptions import ValidationError
from .models import *
from .utils import get_current_user
 
 
class EtudiantForm(forms.ModelForm):
 
	class Meta:
		model = Etudiant
		fields = "__all__"
		widgets = {
			'nom': forms.TextInput(attrs={'class': 'selectpicker form-control',
											'placeholder': 'Entrez nom'}),
			'prenom': forms.TextInput(attrs={'class': 'selectpicker form-control',
														'placeholder': 'Entrez prenom'}),
			'sexe': forms.TextInput(attrs={'class': 'selectpicker form-control',
														'placeholder': 'Entrez votre sexe'}),
			'telephone': forms.TextInput(attrs={'class': 'selectpicker form-control',
											'placeholder': 'Entrez telephone'}),
			}

class EnseignantForm(forms.ModelForm):
 
	class Meta:
		model = Enseignant
		fields = "__all__"
		widgets = {
			'nom': forms.TextInput(attrs={'class': 'selectpicker form-control',
											'placeholder': 'Entrez nom'}),
			'prenom': forms.TextInput(attrs={'class': 'selectpicker form-control',
														'placeholder': 'Entrez prenom'}),
			'sexe': forms.TextInput(attrs={'class': 'selectpicker form-control',
														'placeholder': 'Entrez votre sexe'}),
			'telephone': forms.TextInput(attrs={'class': 'selectpicker form-control',
											'placeholder': 'Entrez telephone'}),
			}

class PersonnelForm(forms.ModelForm):
 
	class Meta:
		model = Personnel
		fields = "__all__"
		widgets = {
			'nom': forms.TextInput(attrs={'class': 'selectpicker form-control',
											'placeholder': 'Entrez nom'}),
			'prenom': forms.TextInput(attrs={'class': 'selectpicker form-control',
														'placeholder': 'Entrez prenom'}),
			'sexe': forms.TextInput(attrs={'class': 'selectpicker form-control',
														'placeholder': 'Entrez votre sexe'}),
			'telephone': forms.TextInput(attrs={'class': 'selectpicker form-control',
											'placeholder': 'Entrez telephone'}),
			}


class VisiteurForm(forms.ModelForm):

	class Meta:
		model = Visiteur
		fields = "__all__"
		widgets = {
			'nom': forms.TextInput(attrs={'class': 'selectpicker form-control',
											'placeholder': 'Entrez nom'}),
			'prenom': forms.TextInput(attrs={'class': 'selectpicker form-control',
														'placeholder': 'Entrez prenom'}),
			'sexe': forms.TextInput(attrs={'class': 'selectpicker form-control',
														'placeholder': 'Entrez votre sexe'}),
			'telephone': forms.TextInput(attrs={'class': 'selectpicker form-control',
											'placeholder': 'Entrez telephone'}),
		}


class VisiteForm(forms.ModelForm):
	class Meta:
		model = Visite
		fields = ("visiteur", 'motif',"heure_depart")
		widgets = {
			'visiteur': forms.Select(attrs={'class': 'selectpicker form-control',}),
			'motif': forms.Textarea(attrs={'class': 'selectpicker form-control',
											'placeholder': 'Motif de la visite'}),
		}