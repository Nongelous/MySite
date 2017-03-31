#from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Helloka nyaloka, a modul muxik!")	
# Create your views here.
