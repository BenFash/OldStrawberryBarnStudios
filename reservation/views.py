from django.shortcuts import render, get_object_or_404, reverse
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from .models import Room, Reservation


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