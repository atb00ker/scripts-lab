from django.http import HttpResponse
from django.shortcuts import render
from .models import Album
# Create your views here.
def index(request):
    # all_albums = Album.object.all()
    context = {'all_albums': 'all_albums'}
    return render(request, 'index.html')

def details(request, album_id):
    context = {'album_id': album_id }
    return render(request, 'details.html', context)
