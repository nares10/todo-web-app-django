from django.shortcuts import render, redirect 
from .models import Todo
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

@login_required
def home(request):
    todos = Todo.objects.filter(user=request.user)  # Fetch all todo items from the database
    context = {
        'todos': todos,
        'user': request.user,
    }
    return render(request, 'todoapp/home.html', context)

@login_required
def add_todo(request):
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        if not title:
            messages.error(request, 'Task title cannot be blank.')
            return redirect('home')
        Todo.objects.create(title=title, user=request.user)
        return redirect('home')
    return render(request, 'todoapp/home.html')

@login_required
def toggle(request):
    if request.method == 'POST':
        todo_id = request.POST.get('todo_id')
        todo = Todo.objects.get(id=todo_id, user=request.user) # Only get todo for current user
        todo.completed = not todo.completed  # Toggle the completed status
        todo.save()
        return redirect('home')
    return render(request, 'todoapp/home.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return redirect('register')
        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return redirect('home')
    return render(request, 'todoapp/register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    return render(request, 'todoapp/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')