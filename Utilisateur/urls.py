from django.urls import path
from . import views

urlpatterns = [
    path('accueil/', views.accueil, name='accueil'),
    path('deconnexion-client/', views.deconnexion_client, name='deconnexion_client'),

    path('client/inscription/', views.inscription_client_view, name='inscription_view'),
    path('inscription_client/', views.inscription_client, name='inscription_client'),
    
    path('connexion/', views.connexion_view, name='connexion_view'),
    path('connexion/', views.connexion, name='connexion'),

    path('professeur/inscription/', views.inscription_prof_view, name='inscription_prof_view'),
    path('inscription_prof/', views.inscription_prof, name='inscription_professeur'),

]