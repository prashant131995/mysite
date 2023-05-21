from django.contrib import admin
from django.urls import path
from Home import views

urlpatterns = [
    path('',views.index,name='home'),
    path('about',views.about,name='about'),
    path("Dell",views.Dell,name="Dell"),
    path("hp",views.hp,name="hp"),
    path("Lenovo",views.Lenovo,name="Lenovo")

]
