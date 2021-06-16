from django.shortcuts import render
from .models import Pokemon #import Pokemon Data

# View functions
def home(request):
    return HttpResponse('<h1> Pokemon Collector </h1>')

def about(request):
    return render(request, 'about.html')

def pokemon_index(request):
   pokemon = Pokemon.objects.all() #query
   return render(request, 'pokemon/index.html', {'pokemons': pokemon})