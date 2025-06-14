from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Ticket, Comment
from django.contrib.auth.models import User
from django.db import IntegrityError

def frontend(request):
    if request.user.is_authenticated:
        return render(request, 'dashboard.html')
    return render(request, 'index.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('frontend')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('frontend')

@login_required
def create_ticket(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        class_name = request.POST.get('class_name')
        
        if not class_name:
            messages.error(request, 'Please select a class.')
            return render(request, 'create_ticket.html')
        
        Ticket.objects.create(
            title=title,
            description=description,
            class_name=class_name,
            created_by=request.user
        )
        messages.success(request, 'Ticket created successfully!')
        return redirect('my_tickets')
    return render(request, 'create_ticket.html')

@login_required
def my_tickets(request):
    tickets = Ticket.objects.filter(created_by=request.user).prefetch_related('comments__user')
    return render(request, 'my_tickets.html', {'tickets': tickets})

@login_required
def ticket_detail(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id, created_by=request.user)
    comments = ticket.comments.all()
    return render(request, 'ticket_detail.html', {'ticket': ticket, 'comments': comments})

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        if password != confirm_password:
            messages.error(request, 'Passwords do not match.')
            return render(request, 'register.html')
        
        if len(password) < 6:
            messages.error(request, 'Password must be at least 6 characters long.')
            return render(request, 'register.html')
        
        try:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name
            )
            messages.success(request, 'Registration successful! Please login.')
            return redirect('login')
        except IntegrityError:
            messages.error(request, 'Username already exists.')
            
    return render(request, 'register.html')
