from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def hello_world(request):
    if request.method == "POST" or request.method == 'post':
        # return render(request, 'accountapp/hello_world.html', context={'text': 'POST method!!'})
        return render(request, 'accountapp/hello_world.html', context={'text': 'post method!!'})

    else:
        return render(request, 'accountapp/hello_world.html', context={'text': 'get method!!'})
