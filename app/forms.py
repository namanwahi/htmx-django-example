from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from app.models import User, Post


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["email", "password1", "password2"]


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content"]
