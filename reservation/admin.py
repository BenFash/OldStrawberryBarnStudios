from django.contrib import admin
from .models import Room, RoomImage, Reservation

# Register your models here.
class RoomImageAdmin(admin.StackedInline):
    model = RoomImage

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_name',)
    search_fields = ('room_name',)
    inlines = [RoomImageAdmin]

    class meta:
        model = Room

@admin.register(RoomImage)
class RoomImageAdmin(admin.ModelAdmin):
    pass

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('room', 'check_in', 'check_out', 'guest_name', 'guest_email', 'guest_phone', 'reservation_date', 'reservation_status',)
    search_fields = ('room', 'check_in', 'check_out', 'guest_name', 'guest_email', 'guest_phone', 'reservation_date', 'reservation_status',)