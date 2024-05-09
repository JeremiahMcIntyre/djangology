from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.log_in, name='login'),
    path('signup_nav/', views.sign_up_nav, name='sign_up_nav'),
    path('signup/', views.sign_up, name='sign_up'),
    path('play-song/<str:song_name>/', views.play_song, name='play_song'),
    path('playlists/', views.playlists, name='playlists')
]

