from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register ,name='register'),
    path('registered', views.registered ,name='registered'),
    path('registereder', views.registereder ,name='registereder'),
    path('', views.login ),
    path('signout', views.logout ,name='signout')
    ]