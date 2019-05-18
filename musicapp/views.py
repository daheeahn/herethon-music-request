from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Music

# Create your views here.
def home(request):
    return render(request, 'home.html')

def apply(request):
    artist = request.POST['artist']
    title = request.POST['title']

    music = Music()
    music.artist = artist
    music.title = title
    music.date = timezone.datetime.now()
    music.save()

    return redirect('/')

def manage(request):
    allmusic = Music.objects.all()

    return render(request, 'manage.html', {'allmusic': allmusic})