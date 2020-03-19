#The use of forms.py is to place and describe all form codes for 
# easy maintainability. 
from django import forms
from .models import Place

class NewPlaceForm(forms.ModelForm):
    class Meta: #Tell django which model should be used to create "model = place".
        model = Place 
        fields = ('name', 'visited')
