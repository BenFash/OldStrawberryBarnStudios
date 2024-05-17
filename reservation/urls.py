from django.urls import path
from . import views

urlpatterns = [
    path('', views.RoomsView, name='rooms'),
    path('<int:pk>/', views.RoomDetailView, name='room_detail'),
    path('reservation/<int:pk>/', views.ReservationView, name='reservation'),    
]