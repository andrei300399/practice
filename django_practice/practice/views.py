from django.shortcuts import render

from django.http import HttpResponse
from .models import Riddle

def index(request):
    p = Riddle.objects.count()
    return HttpResponse(f"Hello, {p}World!")