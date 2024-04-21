from django.shortcuts import render
from django.http import FileResponse
from django.conf import settings

import os

def login(request):
    return render(request, 'player/login.html')

def play_page(request):
    return render(request, 'player/play_page.html')

def play_song(request, song_name):
    song_path = os.path.join(settings.MEDIA_ROOT, song_name)
    return FileResponse(open(song_path, 'rb'), content_type='audio/mpeg')
