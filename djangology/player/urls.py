from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.log_in, name='login'),
    path('play-song/<str:song_name>/', views.play_song, name='play_song'),
    path('play/', views.play_page, name='play_page')
]

