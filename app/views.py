from django.http import HttpResponse
from django.http.response import HttpResponse
from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic import FormView, TemplateView
from django.contrib.auth import get_user_model
from .forms import RegisterForm


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
