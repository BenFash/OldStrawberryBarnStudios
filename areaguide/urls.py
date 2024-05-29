from django.urls import path
from . import views

urlpatterns = [
    path('', views.AreaGuide, name='areaguide'),
]