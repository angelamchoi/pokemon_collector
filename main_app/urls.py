from django.urls import path
from . import views

urlpatterns =[
    path('', views.home, name='home'), #homepage
    path('about/', views.about, name='about'), #about
    path('pokemon/', views.pokemon_index, name='index'), #pokemons
    path('pokemon/<int:pokemon_id>/', views.pokemon_detail, name='detail'), #details
]