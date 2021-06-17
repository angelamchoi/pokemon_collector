from django.urls import path
from . import views

urlpatterns =[
    path('', views.home, name='home'), #homepage
    path('about/', views.about, name='about'), #about
    path('pokemon/', views.pokemon_index, name='index'), #pokemons
    path('pokemon/<int:pokemon_id>/', views.pokemon_detail, name='detail'), #details
    path('pokemon/create', views.PokemonCreate.as_view(), name ='pokemon_create'), #create CBV
    path('pokemon/<int:pk>/update/', views.PokemonUpdate.as_view(), name='pokemon_update'), #update
    path('pokemon/<int:pk>/delete/', views.PokemonDelete.as_view(), name='pokemon_delete'), #delete
]

#### Notes #####
# pk = primary key
# we need pk for CBV