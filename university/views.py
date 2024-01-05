# -*- coding: utf-8 -*-
from django.views.generic import ListView, DetailView 
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from django.urls import reverse_lazy

from .models import University
from .forms import UniversityForm

class UniversityList(ListView):
    model = University

class Universityindex(ListView):
    model = University
    template_name = 'university/home.html'
class UniversityDetail(DetailView):
    model = University

class UniversityMoreDetail(DetailView):
    model = University
    template_name = 'university/university_moredetail.html'
class UniversityCreate(SuccessMessageMixin, CreateView):
    model = University
    form_class = UniversityForm
    success_url = reverse_lazy('university_list')
    success_message = "University successfully created!"

class UniversityUpdate(SuccessMessageMixin, UpdateView):
    model = University
    form_class = UniversityForm
    success_url = reverse_lazy('university_list')
    success_message = "University successfully updated!"

class UniversityDelete(SuccessMessageMixin, DeleteView):
    model = University
    success_url = reverse_lazy('university_list')
    success_message = "University successfully deleted!"


