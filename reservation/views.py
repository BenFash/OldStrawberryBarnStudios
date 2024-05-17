from django.core.mail import send_mail
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from .models import Room, RoomImage, Reservation
from .forms import ReservationForm


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

    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.room = room
            reservation.save()

            # Email details
            subject = f'New Reservation Enquiry for {room.room_name}'
            message = f'''
            Reservation Details
            Room: {room.room_name}
            Check-in Date: {reservation.check_in}
            Check-out Date: {reservation.check_out}
            Guest Name: {reservation.guest_name}
            Guest Email: {reservation.guest_email}
            Guest Phone: {reservation.guest_phone}
            Number of Guests: {reservation.num_guests}
            Number of Dogs: {reservation.dog}
            Vehicle: {'Yes' if reservation.vehicle else 'No'}
            Additional Information: {reservation.guest_info}
            '''
            from_email = reservation.guest_email
            recipient_list = ['benfashan71@msn.com']  # Replace with your correct email

            # Send email notification to yourself
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)

            # Add a success message
            messages.success(request, f'Please expect contact from the owners within 3 working days regarding your enquiry about the availability of {room.room_name}.')

            # Redirect to the room details page using pk
            return redirect('room_detail', pk=room.pk)
    else:
        form = ReservationForm(initial={'room': room})

    return render(request, 'reservation/reservation_form.html', {'form': form, 'room': room})
