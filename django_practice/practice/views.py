from django.shortcuts import render

from django.http import HttpResponse
from .models import Post


def index(request):
    post_list = Post.objects.order_by('title')
    return render(request, 'practice/index.html', {'post_list': post_list})
