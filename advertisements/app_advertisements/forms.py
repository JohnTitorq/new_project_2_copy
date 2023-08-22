from django import forms 
from django.forms import ModelForm
from pydantic import ValidationError
from app_advertisements.models import *


class AdvertisementForm(ModelForm):
    class Meta:
        model=Advertisement
        fields=['title', 'description', 'price', 'auction', 'image']
        widgets={

            'title': forms.TextInput(attrs={
                              'class': 'form-control'
                              }),

            'description': forms.Textarea(attrs={
                              'class': 'form-control'
                          }),

            'price': forms.NumberInput(attrs={
                              'class': 'form-control'
                          }),
            
            'auction': forms.CheckboxInput(attrs={
                              'class': 'form-check-input'
                          }),
            
            'image': forms.FileInput(attrs={
                              'class': 'form-control'
                          })

        }

