from django.http import HttpResponse
from django.shortcuts import render
from .models import Post
from django.shortcuts import render, get_object_or_404


def index(request):
    posts = Post.objects.all()  # Fetch all posts from the database
    return render(request, "index.html", {"posts": posts})


def post_page(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, "post.html", {"post": post})
