from django.http import HttpResponse
from .models import Ticket

from django.utils import timezone


def index(request):
    return HttpResponse("TODO: show some stats....")

def valid(request):
    code = request.GET.get('c', None)
    if not code:
        return HttpResponse(0)

    t = Ticket.objects.filter(code=code).first()
    if not t:
        return HttpResponse(0)

    if t.redeemed:
        return HttpResponse(0)

    if t.validto and t.validto < timezone.localtime(timezone.now()).date():
        return HttpResponse(0)

    return HttpResponse(1)
    

def redeem(request):
    code = request.GET.get('c', None)
    if not code:
        return HttpResponse(0)

    t = Ticket.objects.filter(code=code).first()
    if not t:
        return HttpResponse(0)

    if t.redeemed:
        return HttpResponse(0)

    if t.validto and t.validto < timezone.localtime(timezone.now()).date():
        return HttpResponse(0)

    t.redeemed = timezone.localtime(timezone.now())
    t.save()

    return HttpResponse(1)