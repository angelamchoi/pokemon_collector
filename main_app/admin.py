from django.contrib import admin
from .models import Pokemon, Feeding, Photo

# Register models
admin.site.register(Pokemon)
admin.site.register(Feeding)
admin.site.register(Photo)
