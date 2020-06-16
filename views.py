from django.http import HttpResponse

counter_track = 0


def hello(request): 
    return HttpResponse("Hello World")


def bye(request):
    return HttpResponse("bye")

def counter(request): 
    global counter_track
    counter_track += 1
    return HttpResponse(f'<div id="counter">{counter_track}</div>')