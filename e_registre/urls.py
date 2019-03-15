from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'e_registre'

urlpatterns = [
	path('', views.home, name='home'),
	path('ajouter/<categorie>/', views.add_personne, name='ajouter'),
	path('<categorie>/<int:id>/', views.detail, name='detail'),
	path('liste/<categorie>/', views.liste, name='liste'),
	path('now', views.date_is, name="heure"),

	# ********** AJAX REQUEST URLs*******************
	path('visites/nouveau/<categorie>/<int:id>/', views.debut_visite),
	path('visites/fin/<categorie>/<int:id>/', views.fin_visite),
	
]