from django.shortcuts import render, redirect #import render and redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView #import all views
from django.views.generic import ListView, DetailView # import listview and detailview for toy
from django.contrib.auth import login #login
from django.contrib.auth.forms import UserCreationForm #form
from django.contrib.auth.decorators import login_required #@login_required
from django.contrib.auth.mixins import LoginRequiredMixin #login required mixin

# AWS
import uuid #generates random string
import boto3

from .models import Pokemon, Toy, Photo #import Pokemon, Toy, Photo
from . forms import FeedingForm #import feeding data

# Constant variables 
S3_BASE_URL = 'https://s3.us-west-1.amazonaws.com/'
BUCKET = 'pokemoncollector12345'

### Pokemon CBV ###
def signup(request):
    error_message = ''
    if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
      # This will add the user to the database
            user = form.save()
      # This is how we log a user in via code
        login(request, user)
        return redirect('index')
    else:
        error_message = 'Invalid credentials - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)



# Create
class PokemonCreate(LoginRequiredMixin, CreateView):
    model = Pokemon
    fields = ['name', 'breed', 'abilities', 'number']
    success_url= '/pokemons/'
    def form_valid(self, form):
        # Assign the logged in user (self.request.user)
        form.instance.user = self.request.user  # form.instance is the pokemon
    # Let the CreateView do its job as usual
        return super().form_valid(form)

# Update
class PokemonUpdate(LoginRequiredMixin, UpdateView):
    model = Pokemon
    fields= ['breed', 'abilities', 'number']

# Delete
class PokemonDelete(LoginRequiredMixin, DeleteView):
    model = Pokemon
    success_url= '/pokemons/'

# View functions
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def pokemons_index(request):
    pokemons = Pokemon.objects.filter(user=request.user)
    return render(request, 'pokemons/index.html', { 'pokemons': pokemons})

@login_required
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

@login_required
def add_feeding(request, pokemon_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.pokemon_id = pokemon_id
        new_feeding.save()
    return redirect('detail', pokemon_id=pokemon_id)

@login_required
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

@login_required
def assoc_toy(request, pokemon_id, toy_id):
    Pokemon.objects.get(id=pokemon_id).toys.add(toy_id)
    return redirect('detail', pokemon_id=pokemon_id)

@login_required
def unassoc_toy(request, pokemon_id, toy_id):
    Pokemon.objects.get(id=pokemon_id).toys.remove(toy_id)
    return redirect('detail', pokemon_id=pokemon_id)