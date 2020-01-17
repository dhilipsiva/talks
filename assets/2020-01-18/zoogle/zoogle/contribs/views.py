from django.shortcuts import render
from django.http import JsonResponse

from zoogle.zmail.models import Zmail
from zoogle.zdocs.models import Zdoc


def index(request):
    return render(request, 'index.html')


def ssr(request):
    zmails = Zmail.objects.all()
    zdocs = Zdoc.objects.all()
    ctx = dict(zmails=zmails, zdocs=zdocs)
    return render(request, 'ssr.html', ctx)


def ajax(request):
    return render(request, 'ajax.html')


def search(request):
    return render(request, 'search.html')


def zdocs(request):
    return JsonResponse({})


def zmail(request):
    return JsonResponse({})
