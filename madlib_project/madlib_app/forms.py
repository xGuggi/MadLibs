from django import forms
from .models import Madlib


class MadLibForm(forms.ModelForm):
    class Meta:
        model = Madlib
        fields = ['name', 'time', 'noun', 'pronoun', 'adjective', 'place', 'verb']
