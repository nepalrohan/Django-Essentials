from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.
from .models import Room
# rooms =[
#     {"id":1, "name":"Rohan"},
#     {"id":2, "name":"Hari"},
#     {"id":3, "name":"Bishal"},
# ]


def home(request):
    rooms = Room.objects.all()
    return render(request, 'base/home.html', {'rooms':rooms})

def room(request, pk):
    room=Room.objects.get(id=pk)

    context = {'room':room}
    return render(request, 'base/room.html', context)


