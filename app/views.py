from django.http import HttpResponse
from django.http.response import HttpResponse
from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic import FormView, TemplateView, ListView
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.contrib.auth import get_user_model
from .forms import RegisterForm, PostForm
from .models import Post
from django.shortcuts import render
from django.http import Http404
from django.core.exceptions import PermissionDenied


class IndexView(TemplateView):
    template_name = "index.html"


class RegisterView(FormView):
    form_class = RegisterForm
    template_name = "register.html"
    success_url = reverse_lazy("app:login")

    def form_valid(self, form):
        form.save()  # save the user
        return super().form_valid(form)


def check_email(request):
    email = request.POST.get("email")
    if get_user_model().objects.filter(email=email).exists():
        return HttpResponse(
            "<div id='email-error' class='error'>This email already exists</div>"
        )
    else:
        return HttpResponse(
            "<div id='email-error' class='success'>This email is available</div>"
        )


@login_required
def post_list_view(request):
    posts = Post.objects.filter(user=request.user).order_by("-date_posted")
    form = PostForm()
    context = {
        "posts": posts,
        "form": form,
    }
    return render(request, "posts.html", context)


@require_http_methods(["POST"])
@login_required
def add_post(request):
    form = PostForm(request.POST)
    if form.is_valid():
        post = form.save(commit=False)
        post.user = request.user
        post.save()
    return render(
        request,
        "partials/post_list.html",
        context={
            "posts": Post.objects.filter(user=request.user).order_by("-date_posted")
        },
    )


@require_http_methods(["DELETE"])
@login_required
def delete_post(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        raise Http404("Post does not exist")

    if post.user != request.user:
        raise PermissionDenied("You are not allowed to delete this post")

    post.delete()
    return render(
        request,
        "partials/post_list.html",
        context={
            "posts": Post.objects.filter(user=request.user).order_by("-date_posted")
        },
    )
