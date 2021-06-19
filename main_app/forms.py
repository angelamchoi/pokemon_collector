from django.forms import ModelForm
from .models import Feeding

class FeedingForm(ModelForm):
    class Meta:
        model = Feeding
        fields = ['date', 'meal']

### Notes ###
# ModelForm
#-->1. generate forms
#-->2. validates submitted form
#-->3. saves data in the data base