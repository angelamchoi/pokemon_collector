from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView #import all views
from .models import Pokemon #import Pokemon Data

# View functions
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def pokemons_index(request):
    pokemons = Pokemon.objects.all()
    return render(request, 'pokemons/index.html', { 'pokemons': pokemons})

def pokemons_detail(request, pokemon_id):
    pokemon = Pokemon.objects.get(id=pokemon_id)
    return render(request, 'pokemons/detail.html', { 'pokemon': pokemon })

### Pokemon CBV ###

# Create
class PokemonCreate(CreateView):
    model = Pokemon
    fields = '__all__'
    success_url='/pokemons/'

# Update
class PokemonUpdate(UpdateView):
    model = Pokemon
    fields= ['breed', 'abilities', 'number']

# Delete
class PokemonDelete(DeleteView):
    model = Pokemon
    success_url= '/pokemons/'

