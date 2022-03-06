from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context_dict = {}
    return render(request, 'rerig/index.html', context=context_dict)


def about(request):
    context_dict = {}
    return render(request, 'rerig/about.html', context=context_dict)
# Create your views here.
