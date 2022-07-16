from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm, UserForm
from django.contrib import messages


# Create your views here.


def signup(request):

    if request.user.is_authenticated:
        return redirect('tasks')

    form = UserForm()

    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    context = {'form': form}
    return render(request, 'registration/signup.html', context)


@login_required
def tasks(request):
    tasks = Task.objects.filter(user=request.user)
    incomplete_task_count = tasks.filter(complete=False).count()

    if request.method == "GET":
        search_input = request.GET.get('search-area') or ''
        if search_input:
            tasks = tasks.filter(title__icontains=search_input)

    context = {'tasks': tasks, 'incomplete_task_count': incomplete_task_count, 'search_input': search_input}
    return render(request, 'tasks.html', context)


@login_required
def task(request,pk):
    task = Task.objects.get(id=pk)
    context = {'task': task}
    return render(request, 'task.html', context)


@login_required
def create_task(request):

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect('tasks')

    form = TaskForm()
    context = {'form': form}
    return render(request, 'create_task.html', context)


@login_required
def edit_task(request,pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('tasks')

    context = {'form': form}
    return render(request, 'create_task.html', context)


@login_required
def delete_task(request,pk):
    task = Task.objects.get(id=pk)

    if request.method == "POST":
        task.delete()
        return redirect('tasks')

    context = {'task':task}
    return render(request, 'delete_task.html', context)


@login_required
def delete_tasks(request):
    tasks = Task.objects.filter(user=request.user)
    tasks.delete()

    return redirect('tasks')


@login_required
def delete_complete_tasks(request):
    tasks = Task.objects.filter(user=request.user)
    complete_tasks = tasks.filter(complete=True)
    complete_tasks.delete()

    return redirect('tasks')