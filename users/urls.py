from django.contrib import admin
from django.urls import path, include
from .views import user_signup, user_logout, user_login
urlpatterns = [
    path('signup/', user_signup, name='user_signup'),
    path('login/', user_login, name='user_login'),
    path('logout/', user_logout, name='user_logout'),
]

