from django.shortcuts import render

# Create your views here.
def index(request):
    body = '<h2>HOME</h2>'
    context = {
        'body': body
    }
    return render(request, 'summoner/index.html', context)
