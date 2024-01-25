# forms.py
from django import forms
from .models import User
from teams.models import User, Location, Role

class UserSelectionForm(forms.Form):
    user = forms.ModelChoiceField(queryset=User.objects.all(), empty_label=None)
