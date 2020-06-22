from counter.models import Counter
from django.shortcuts import render


def hello(request):
    return render(request, 'hello.html')


def bye(request):
    return render(request, 'bye.html')


def counter(request):
    counter, created = Counter.objects.get_or_create(id=1)
    counter.value += 1
    counter.save()
    context = {
        'counter': counter
    }
    return render(request, 'counter.html', context)
