from django.db import models

# pokemon model
class Pokemon(models.Model):
    name = models.CharField(max_length =100)
    breed = models.CharField(max_length=100)
    abilities = models.TextField(max_length=250)
    number = models.IntegerField()

# use str method 
    def __str__(self):
        return self.name

