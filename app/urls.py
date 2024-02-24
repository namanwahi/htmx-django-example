from django.urls import path

from . import views

app_name = "app"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:post_id>/", views.post_page, name="post_page"),
]
