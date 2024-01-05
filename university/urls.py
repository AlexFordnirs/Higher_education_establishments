# -*- coding: utf-8 -*-
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Universityindex.as_view(), name='index'),
    path('list', views.UniversityList.as_view(), name='university_list'),
    path('view/<int:pk>', views.UniversityDetail.as_view(), name='university_view'),
    path('new', views.UniversityCreate.as_view(), name='university_new'),
    path('edit/<int:pk>', views.UniversityUpdate.as_view(), name='university_edit'),
    path('delete/<int:pk>', views.UniversityDelete.as_view(), name='university_delete'),
    path('university/detail/<int:pk>', views.UniversityMoreDetail.as_view(), name='university_moredetail'),
]