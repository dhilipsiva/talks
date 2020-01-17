from django.shortcuts import render
from django.http import JsonResponse

from zoogle_pb2 import Void, Query
from zoogle.zdocs.models import Zdoc
from zoogle.zmail.models import Zmail
from zoogle.contribs.clients.zmail import zmail_stub
from zoogle.contribs.clients.zdocs import zdocs_stub


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
    query = request.GET.get('query', '')
    query = Query(text=query)
    results = list(zdocs_stub.Search(query))
    results += list(zmail_stub.Search(query))
    ctx = dict(results=results, query=query.text)
    return render(request, 'search.html', ctx)


def zdocs(request):
    docs = []
    for doc in zdocs_stub.Docs(Void()):
        docs.append(dict(
            subject=doc.subject, description=doc.description,
            owner=doc.owner, size=doc.size))
    return JsonResponse({'data': docs})


def zmail(request):
    mails = []
    for mail in zmail_stub.Mails(Void()):
        mails.append(dict(
            subject=mail.subject, description=mail.description,
            from_addr=mail.from_addr, to_addr=mail.to_addr))
    return JsonResponse({'data': mails})
