from django.shortcuts import render
from django.http import JsonResponse


def index(request):
    return render(request, 'index.html')


def ssr(request):
    return render(request, 'ssr.html')


def ajax(request):
    return render(request, 'ajax.html')


def search(request):
    return render(request, 'search.html')


def zdocs(request):
    return JsonResponse({})


def zmail(request):
    return JsonResponse({})
