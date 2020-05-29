from django.shortcuts import render

from quote.models import Quote


def index(request):
    return render(request, 'quote/index.html', {
        'quotes': Quote.objects.all(),
    })
