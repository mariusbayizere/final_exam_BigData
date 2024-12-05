from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import User
from .forms import UserForm


def user_list(request):
    """List all users."""
    users = User.objects.all()
    return render(request, 'users/user_list.html', {'users': users})


def user_detail(request, pk):
    """Display details of a single user."""
    user = get_object_or_404(User, pk=pk)
    return render(request, 'users/user_detail.html', {'user': user})


def user_create(request):
    """Create a new user."""
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm()
    return render(request, 'users/user_form.html', {'form': form})


def user_update(request, pk):
    """Update an existing user."""
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm(instance=user)
    return render(request, 'users/user_form.html', {'form': form})


def user_delete(request, pk):
    """Delete a user."""
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('user_list')
    return render(request, 'users/user_confirm_delete.html', {'user': user})
