from django.http import HttpResponse
from datetime import datetime


def hello_world(request):

    return HttpResponse('Hello World the time now is {now}'. format(
        now=datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
        ))

def hi(request):
    numbers = map(int, request.GET["numbers"].split(","))
    return 