from django.shortcuts import render
rooms = [
    {'id':1, 'name':'파이썬을 배워봅시다.'},
    {'id':2, 'name':'디자인도 해봅시다..'},
    {'id':3, 'name':'프론트엔드 개발자.'},
    {'id':4, 'name':'백엔드 개발자.'},
]

def home(request):
    context = {'rooms': rooms}
    return render(request, 'main/home.html', context)

def room(request, pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
    context = {'room' : room}

    return render(request, 'main/room.html', context)
