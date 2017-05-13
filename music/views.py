from django.http import HttpResponse

def index(requests):
    return HttpResponse("<h1>This is the Music app homepage</h1>")