from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# Create your models here.


class Matiere(models.Model):
	libelle = models.CharField(max_length=50, default="M")

	def __str__(self):
		return self.libelle

class Personne(models.Model):
	nom = models.CharField(max_length=50)
	prenom = models.CharField(max_length=50)
	sexe = models.CharField(max_length=1)
	telephone = models.CharField(max_length=100)
	
	def __str__(self):
		return f"{self.nom}"

class Visiteur(Personne):

	def __str__(self):
		return f"{self.nom}"

class Etudiant(Personne):
	filiere = models.ForeignKey('Filiere', on_delete=models.CASCADE, null=True)
	def __str__(self):
		return f"{self.nom}"

class Personnel(Personne):
	departement = models.ForeignKey('Departement', on_delete=models.CASCADE, null=True)
	def __str__(self):
		return f"{self.nom}"

class Enseignant(Personne):
	matieres = models.ManyToManyField(Matiere, through='Enseignement', related_name='+')
	def __str__(self):
		return f"{self.nom}"

class Visite(models.Model):
	visiteur = models.ForeignKey('Personne', on_delete=models.CASCADE)
	date_de_visite = models.DateField(default=timezone.now)
	heure_darrive = models.TimeField(default=timezone.now)
	heure_depart = models.TimeField(null=True, blank=True)
	motif = models.TextField(null=True, blank=True)

	def __str__(self):
		return self.visiteur.nom

class Filiere(models.Model):
	libelle = models.CharField(max_length=50)

	def __str__(self):
		return self.libelle

class Departement(models.Model):
	libelle = models.CharField(max_length=50)

	def __str__(self):
		return self.libelle

class Enseignement(models.Model):
	matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE)
	enseignant = models.ForeignKey(Enseignant, on_delete=models.CASCADE)

	def __str__(self):
		return f"{self.enseignant.libelle} enseigne {self.matiere.libelle}"