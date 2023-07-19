from django.shortcuts import render
from .models import Room

"""
rooms = [
    {'id':1, 'name':'파이썬을 배워봅시다.'},
    {'id':2, 'name':'디자인도 해봅시다..'},
    {'id':3, 'name':'프론트엔드 개발자.'},
    {'id':4, 'name':'백엔드 개발자.'},
]
"""

def home(request):
    rooms = Room.objects.all()    #model 매니저
    context = {'rooms': rooms}
    return render(request, 'main/home.html', context)

def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room' : room}

    return render(request, 'main/room.html', context)
