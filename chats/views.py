from django.shortcuts import render

from .models import Message,User

def index(request):
    latest_messages = Message.objects.order_by('-timestamp')[:5]
    context = {
    'latest_messages': latest_messages,
    }
    return render(request, 'chats/index.html', context)


def room(request, room_name):
    if room_name == 'general':
        return render(request, 'chats/general.html', { 'room_name': room_name})
    else:
        return render(request, 'chats/404.html', { 'room_name': room_name})
