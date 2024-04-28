from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import FileResponse
from django.conf import settings
from .models import Users

import os

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('play_page')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'player/login.html')

def play_page(request):
    return render(request, 'player/play_page.html')

def play_song(request, song_name):
    song_path = os.path.join(settings.MEDIA_ROOT, song_name)
    return FileResponse(open(song_path, 'rb'), content_type='audio/mpeg')

def play_page(request):
    user = Users.objects.get(userId=1)
    context = {'user_name': user.userDisplayName}
    print(context)
    return render(request, 'player/play_page.html', context)