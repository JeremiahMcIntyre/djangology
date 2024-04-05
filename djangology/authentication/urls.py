from django.urls import path, include
from . import views  # Import views if needed

urlpatterns = [
    path('login/', views.login, name='login'),
]

