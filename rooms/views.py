from django.shortcuts import render
from . import models

# from django.http import HttpResponse


# Create your views here.
def all_rooms(request):
    all_rooms = models.Room.objects.all()
    context = {
        "rooms": all_rooms,
    }
    return render(request, "rooms/home.html", context=context)


1
