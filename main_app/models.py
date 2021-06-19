from django.db import models
from django.urls import reverse #reverse

MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner'),
    ('S', 'Snack')
)

# pokemon model
class Pokemon(models.Model):
    name = models.CharField(max_length =100)
    breed = models.CharField(max_length=100)
    abilities = models.TextField(max_length=250)
    number = models.IntegerField()

# use str method 
    def __str__(self):
        return self.name

# Method
    def get_absolute_url(self):
        return reverse('detail', kwargs={'pokemon_id': self.id})

# feeding model
class Feeding(models.Model):
    date = models.DateField('feeding date')
    meal = models.CharField(
        max_length=1,
        choices=MEALS,
        default=MEALS[0][0] #default to be 'B'
    )

    #pokemon FK
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    
    def __str__(self):
        # Nice method for obtaining the friendly value of a Field.choice
        return f"{self.get_meal_display()} on {self.date}"

