from django.shortcuts import render
from django.http import HttpResponse
from .models import Message,User

def index(request):
    latest_messages = Message.objects.order_by('-timestamp')[:5]
    output = ', '.join([m.message_content for m in latest_messages])
    return HttpResponse(output)