from django.db import models
from django.urls import reverse #reverse
from datetime import date # date

# Constants
MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner'),
    ('S', 'Snack')
)

# toy model
class Toy(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('toys_detail', kwargs={'pk': self.id})

# pokemon model
class Pokemon(models.Model):
    name = models.CharField(max_length =100)
    breed = models.CharField(max_length=100)
    abilities = models.TextField(max_length=250)
    number = models.IntegerField()
    toys = models.ManyToManyField(Toy) #M:M relationship

# use str method 
    def __str__(self):
        return self.name

# Method
    def get_absolute_url(self):
        return reverse('detail', kwargs={'pokemon_id': self.id})

    def fed_for_today(self):
        return self.feeding_set.filter(date=date.today()).count() >= len(MEALS)


# feeding model
class Feeding(models.Model):
    date = models.DateField('feeding date')
    meal = models.CharField(
        max_length=1,
        choices=MEALS,
        default=MEALS[0][1] #default to be 'L'
    )
    #pokemon FK
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    
    def __str__(self):
        # Nice method for obtaining the friendly value of a Field.choice
        return f"{self.get_meal_display()} on {self.date}"

    class Meta:
        ordering =['-date']



