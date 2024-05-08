from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.log_in, name='login'),
    path('play-song/<str:song_name>/', views.play_song, name='play_song'),
    path('playlists/', views.playlists, name='playlists')
]

