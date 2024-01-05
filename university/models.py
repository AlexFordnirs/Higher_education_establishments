# -*- coding: utf-8 -*-
from django.db import models
from django.urls import reverse_lazy
class University(models.Model):
    name = models.CharField('Name', max_length=100)
    description = models.TextField('Description', blank=True)
    price = models.DecimalField('Price', decimal_places=2, max_digits=8)
    created = models.DateTimeField('Created', auto_now_add=True)
    changed = models.DateTimeField('Changed', auto_now=True)
    image_url = models.URLField('Image URL', blank=True, default='')
    address = models.TextField('Address', blank=True)
    telephone = models.TextField('Telephone', blank=True)
    email = models.TextField('Email', blank=True)
    website = models.TextField('Website', blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('university_edit', kwargs={'pk': self.pk})
