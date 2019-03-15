from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Etudiant)
admin.site.register(Personnel)
admin.site.register(Enseignant)
admin.site.register(Visiteur)
# admin.site.register(Personne)
admin.site.register(Visite)
admin.site.register(Matiere)
admin.site.register(Filiere)
admin.site.register(Enseignement)
admin.site.register(Departement)