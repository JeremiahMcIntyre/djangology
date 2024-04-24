from django.shortcuts import render
from django.http import FileResponse
from django.conf import settings
from .models import User

import os

def login(request):
    return render(request, 'player/login.html')

def play_page(request):
    return render(request, 'player/play_page.html')

def play_song(request, song_name):
    song_path = os.path.join(settings.MEDIA_ROOT, song_name)
    return FileResponse(open(song_path, 'rb'), content_type='audio/mpeg')

def play_page(request):
    # Assuming User model has a field named 'userDisplayName'
    user = User.objects.get(userId=1)  # Fetching user with ID 1
    context = {'user_name': user.userDisplayName}
    print(context)  # For debugging purposes
    return render(request, 'player/play_page.html', context)