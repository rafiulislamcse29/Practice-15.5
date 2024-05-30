from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('add_musician/',views.add_musician,name='add_musician'),
     path('edit/<int:id>',views.edit_musician,name='editmusician'),
]
