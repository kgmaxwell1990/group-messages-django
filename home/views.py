from django.shortcuts import render
from messenger.models import Message

def get_index(request):
    return render(request, 'home/index.html')