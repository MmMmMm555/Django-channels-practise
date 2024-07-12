from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Room, Message

@login_required
def chat_view(request, room_id):
    rooms = Room.objects.all()
    room = rooms.get(id=room_id)
    messages = Message.objects.filter(room=room)
    return render(request, 'index.html', context={'messages': messages, 'room': room, 'rooms': rooms})
