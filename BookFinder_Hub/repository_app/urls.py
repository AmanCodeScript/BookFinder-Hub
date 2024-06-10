from django.urls import path
from . import views

urlpatterns = [
    path('repository/', views.repository, name='repository'),
]