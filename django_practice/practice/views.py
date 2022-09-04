from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import AddPostForm
from django.urls import reverse



def index(request):
    post_list = Post.objects.values()
    post_form = AddPostForm()
    return render(request, "practice/index.html", {'post_list': post_list, "form": post_form})


def add_post(request):
    if request.method == "POST":
        Post.objects.create(
            title=request.POST["add_title"],
            text=request.POST["add_text"],
            author=request.POST["add_author"],
            count_likes=request.POST["add_count_likes"]
        )
    return HttpResponseRedirect(reverse('practice:index'))


def delete_post(request, post_id=None):
    post_delete = Post.objects.get(id=post_id)
    post_delete.delete()
    return HttpResponseRedirect(reverse('practice:index'))
