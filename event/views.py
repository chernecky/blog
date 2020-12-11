from django.shortcuts import render
from .models import Event

def home(request):
#    event = Event.objects
    return render(request, 'event/home.html')

    # 'event/home.html', {'event': event}
