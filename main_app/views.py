from django.shortcuts import render, redirect #import render and redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView #import all views
from django.views.generic import ListView, DetailView # import listview and detailview for toy

# AWS
import uuid #generates random string
import boto3

from .models import Pokemon, Toy, Photo #import Pokemon, Toy, Photo
from . forms import FeedingForm #import feeding data

# Constant variables 
S3_BASE_URL = 'https://s3.us-west-1.amazonaws.com/'
BUCKET = 'pokemoncollector12345'

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
    # instantiate FeedingForm to be rendered in the template
    feeding_form = FeedingForm()
    toys_pokemon_doesnt_have = Toy.objects.exclude(
        id__in=pokemon.toys.all().values_list('id'))
    return render(request, 'pokemons/detail.html', {
        # pass the pokemon and feeding_form as context
        'pokemon': pokemon, 'feeding_form': feeding_form, 'toys': toys_pokemon_doesnt_have
    })
# In the details page, we want to show the pokemon and feeding form

def add_feeding(request, pokemon_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.pokemon_id = pokemon_id
        new_feeding.save()
    return redirect('detail', pokemon_id=pokemon_id)

def add_photo(request, pokemon_id):
    # photo-file will be the "name" attribute on the <input type="file">
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            # build the full url string
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            # we can assign to pokemon_id or pokemon (if you have a pokemon object)
            photo = Photo(url=url, pokemon_id=pokemon_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect('detail', pokemon_id=pokemon_id)

### Toy CBV ###
class ToyList(ListView):
    model = Toy

class ToyDetail(DetailView):
    model = Toy

class ToyCreate(CreateView):
    model = Toy
    fields = '__all__'

class ToyUpdate(UpdateView):
    model = Toy
    fields = ['name', 'color']

class ToyDelete(DeleteView):
    model = Toy
    success_url = '/toys'

def assoc_toy(request, pokemon_id, toy_id):
    Pokemon.objects.get(id=pokemon_id).toys.add(toy_id)
    return redirect('detail', pokemon_id=pokemon_id)

def unassoc_toy(request, pokemon_id, toy_id):
    Pokemon.objects.get(id=pokemon_id).toys.remove(toy_id)
    return redirect('detail', pokemon_id=pokemon_id)