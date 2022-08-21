from django import forms
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import fields
from django.forms import widgets
from .models import Notes

class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes 
        fields = ('title', 'text')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control my-5'}),
            'text': forms.Textarea(attrs={'class': 'form-control my-5'}),
            
        }
        labels = {
            'text': 'Write your thoughts here:'
        }
    
 
