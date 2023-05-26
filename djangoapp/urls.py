
from .views import index
from django.urls import path
from . import views

urlpatterns = [
    path('', index),
    path('process_input', views.process_input, name='process_input'),
]
