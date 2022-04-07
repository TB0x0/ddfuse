from django.shortcuts import render

from .models import Message,User

def index(request):
    latest_messages = Message.objects.order_by('-timestamp')[:5]
    context = {
    'latest_messages': latest_messages,
    }

    return render(request, 'chats/index.html', context)
