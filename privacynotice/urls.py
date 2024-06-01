from django.urls import path
from . import views

urlpatterns = [
path('', views.PrivacyNoticeView, name='privacynotice'),
]