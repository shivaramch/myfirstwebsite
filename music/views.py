from django.shortcuts import render
from django.http import Http404
from django.conf.urls import include
from django.template import loader
from .models import Album

# Create your views here.
'''def index(request):
    all_objects = Album.objects.all()
    html = ''
    for album in all_objects:
        url = "/music/" + str(album.id) + "/"
        html += '<a href = "' + url + '">' + album.album_title + '</a><br>'
    return HttpResponse(html)
'''


def index(request):
    all_albums = Album.objects.all()
    # template = loader.get_template('music/index.html')
    context = {'all_albums': all_albums}
    return render(request, 'music/index.html', context)
    # return HttpResponse(template.render(context, request))


def detail(request, album_id):
    try:
        album = Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        raise Http404("Album not found!")
    return render(request, 'music/index.html', {'albums': album})
