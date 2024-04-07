from django.shortcuts import render

def login(request):
    return render(request, 'authentication/login.html')

def play_page(request):
    return render(request, 'authentication/play_page.html')