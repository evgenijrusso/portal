from django.shortcuts import render

APP = 'news/'

def index(request):
    return render(request, APP + 'index.html')
