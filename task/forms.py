from django.contrib.auth.models import User
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Task


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'complete']


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email',]
