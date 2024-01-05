# -*- coding: utf-8 -*-
from django import forms

from .models import University

class UniversityForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UniversityForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['description'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['price'].widget.attrs = {
            'class': 'form-control col-md-6',
            'step': 'any',
            'min': '1',
        }
        self.fields['image_url'].widget.attrs = {
            'class': 'form-control col-md-6',
        }
        self.fields['address'].widget.attrs = {
            'class': 'form-control col-md-6',
        }
        self.fields['telephone'].widget.attrs = {
            'class': 'form-control col-md-6',
        }
        self.fields['email'].widget.attrs = {
            'class': 'form-control col-md-6',
        }
        self.fields['website'].widget.attrs = {
            'class': 'form-control col-md-6',
        }

    class Meta:
        model = University
        fields = ('name', 'description', 'price', 'image_url', 'address', 'telephone', 'email', 'website')