from django import forms 
from django.forms import ModelForm
from todoapp.models import *


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class':'txt' ,'placeholder':'Enter List Item Here', 'autocomplete':'off'})
        }