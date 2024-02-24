from django.urls import path
from django.contrib.auth.views import LogoutView, LoginView

from . import views

app_name = "app"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("register/", views.RegisterView.as_view(), name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path(
        "login/",
        views.LoginView.as_view(template_name="login.html"),
        name="login",
    ),
]


htmx_urlpatterns = [path("check_email/", views.check_email, name="check_email")]


urlpatterns += htmx_urlpatterns
