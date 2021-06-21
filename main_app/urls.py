from django.urls import path
from . import views

urlpatterns =[
    path('', views.home, name='home'), #homepage
    path('about/', views.about, name='about'), #about
    path('pokemons/', views.pokemons_index, name='index'), #pokemons
    path('pokemons/<int:pokemon_id>/', views.pokemons_detail, name='detail'), #details
    path('pokemons/create/', views.PokemonCreate.as_view(), name ='pokemons_create'), #create CBV
    path('pokemons/<int:pk>/update/', views.PokemonUpdate.as_view(), name='pokemons_update'), #update
    path('pokemons/<int:pk>/delete/', views.PokemonDelete.as_view(), name='pokemons_delete'), #delete
    path('pokemons/<int:pokemon_id>/add_feeding/', views.add_feeding, name='add_feeding'), #feeding
]

#### Notes #####
# pk = primary key
# we need pk for CBV