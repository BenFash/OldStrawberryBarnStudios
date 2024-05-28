from django.core.mail import send_mail
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from django.http import JsonResponse
from .models import Room, RoomImage, Reservation
from .forms import ReservationForm
import os

# View for rooms page
def RoomsView(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'reservation/rooms.html', context)

# View for room detail page
def RoomDetailView(request, pk):
    room = get_object_or_404(Room, pk=pk)
    room_images = RoomImage.objects.filter(room=room)
    context = {'room': room, 'room_images': room_images}
    return render(request, 'reservation/room_detail.html', context)

# View for making a reservation
def ReservationView(request, pk):
    room = get_object_or_404(Room, pk=pk)
    show_dog_field = room.room_name in ['Orchard View', 'Meadow View']

    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.room = room
            reservation.save()

            # Add a success message
            messages.success(request, f'Please expect contact from the owners within 3 working days regarding your enquiry about the availability of {room.room_name}.')

            # Prepare JSON response
            response_data = {
                'redirect_url': reverse('room_detail', args=[pk]),
                'message': f'Please expect contact from the owners within 3 working days regarding your enquiry about the availability of {room.room_name}.'
            }
            return JsonResponse(response_data)
        else:
            response_data = {'errors': form.errors}
            return JsonResponse(response_data, status=400)
    else:
        form = ReservationForm(initial={'room': room})

    context = {'form': form, 'room': room, 'show_dog_field': show_dog_field}
    return render(request, 'reservation/reservation_form.html', context)
