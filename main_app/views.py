from django.shortcuts import render, redirect #import render and redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView #import all views
from .models import Pokemon #import Pokemon Data
from . forms import FeedingForm #import feeding data

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
    feeding_form = FeedingForm()
    return render(request, 'pokemons/detail.html', { 
        'pokemon': pokemon, 'feeding_form': feeding_form   
    })
    
# In the details page, we want to show the pokemon and feeding form

def add_feeding(request, pokemon_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.pokemon_id = pokemon_id
        new_feeding.save()
    return redirect('detail', pokemon_id=pokemon_id)

### Pokemon CBV ###

# Create
class PokemonCreate(CreateView):
    model = Pokemon
    fields = '__all__'
    success_url= '/pokemons/'

# Update
class PokemonUpdate(UpdateView):
    model = Pokemon
    fields= ['breed', 'abilities', 'number']

# Delete
class PokemonDelete(DeleteView):
    model = Pokemon
    success_url= '/pokemons/'

