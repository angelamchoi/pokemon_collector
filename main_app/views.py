from django.shortcuts import render
from django.http import HttpResponse

#pokemon class
class Pokemon:
    def __init__(self, name, breed, abilities, number):
        self.name = name
        self.breed = breed
        self.abilities = abilities
        self.number = number

#instance
pokemons = [
    Pokemon('Bulbasaur','Grass', 'Overgrow', 1 ),
    Pokemon('Pikachu','Electic', 'Static', 25),
    Pokemon('Snorlax','Normal', 'Immunity', 143),
    Pokemon('Blastoise','Water', 'Torrent', 9),
]

def home(request):
    return HttpResponse('<h1> Pokemon Collector </h1>')

def about(request):
    return render(request, 'about.html')

def pokemon_index(request):
    return render(request, 'pokemon/index.html', {'pokemons': pokemons})