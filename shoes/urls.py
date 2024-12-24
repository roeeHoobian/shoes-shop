from django.contrib import admin
from django.urls import path
from .views import shoes_list, shoe_details, show_homepage, about


urlpatterns = [
    path('', show_homepage, name='home'),
    path('about/', about, name='about'),
    path('home', show_homepage, name='home'),
    path('all', shoes_list, name="shoes_list" ),
    path('shoe-details/<int:id>/', shoe_details, name="shoe_details"),

]
