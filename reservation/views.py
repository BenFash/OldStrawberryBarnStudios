from django.core.mail import send_mail
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import Room, RoomImage, Reservation
from .forms import ReservationForm
import os

# Create your views here.
def RoomsView(request):
    """
    View for rooms page
    """
    rooms = Room.objects.all()

    context = {
        'rooms': rooms,
    }

    return render(request, 'reservation/rooms.html', context)


def RoomDetailView(request, pk):
    """
    View for room detail page
    """
    room = get_object_or_404(Room, pk=pk)
    room_images = RoomImage.objects.filter(room=room)

    context = {
        'room': room,
        'room_images': room_images,
    }

    return render(request, 'reservation/room_detail.html', context)


def ReservationView(request, pk):
    """
    View for making a reservation
    """
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

            # Respond with JSON if the request is an AJAX request
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'redirect_url': reverse('room_detail', args=[pk])})
            
            # Fallback to normal redirect for non-AJAX requests
            return HttpResponseRedirect(reverse('room_detail', args=[pk]))
    else:
        form = ReservationForm(initial={'room': room})

    return render(request, 'reservation/reservation_form.html', {'form': form, 'room': room, 'show_dog_field': show_dog_field})