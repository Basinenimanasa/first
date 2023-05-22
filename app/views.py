from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def srujana(request):
    return HttpResponse('<marquee><h1>srujana tinnavara , Era vadilestunnava </h1></marquee>')
def revi(request):
    return HttpResponse('<marquee><b> mama kutti , Long drive podama </b></marquee>')