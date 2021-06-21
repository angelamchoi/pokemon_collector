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
    path('toys/', views.ToyList.as_view(), name = 'toys_index'),
    path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toys_detail'),
    path('toys/create/', views.ToyCreate.as_view(), name='toys_create'),
    path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toys_update'),
    path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toys_delete'),
    path('cats/<int:cat_id>/assoc_toy/<int:toy_id>/',views.assoc_toy, name='assoc_toy'),
    path('cats/<int:cat_id>/unassoc_toy/<int:toy_id>/', views.unassoc_toy, name='unassoc_toy'),
]

#### Notes #####
# pk = primary key
# we need pk for CBV