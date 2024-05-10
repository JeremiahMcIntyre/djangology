from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import FileResponse
from django.conf import settings
from .models import Users

import os

def log_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('playlists')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'player/login.html')

def sign_up(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        display_name = request.POST.get('displayname')

        if Users.objects.filter(username=username).exists():
            messages.error(request, 'Username is already taken.')
            return redirect('sign_up')

        user = Users.objects.create(username=username, password=password, userDisplayName=display_name)

        auth_login(request, user)
        return redirect('playlists')

    return render(request, 'player/signup.html')

def playlists(request):
    return render(request, 'player/playlists.html')

def sign_up_nav(request):
    return render(request, 'player/signup.html')

def play_song(request, song_name):
    song_path = os.path.join(settings.MEDIA_ROOT, song_name)
    return FileResponse(open(song_path, 'rb'), content_type='audio/mpeg')

