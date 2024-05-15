from django.shortcuts import render, get_object_or_404, reverse
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from .models import Room, RoomImage, Reservation


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