from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .form import UserForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    return render(request, 'index.html')


@login_required
def blog(request):
    post = Post.objects.all()
    return render(request, 'blog.html', {"posts": post})


# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request, f"Account created for {username}")
#             return redirect('blog')
#     else:
#         form = UserCreationForm()
#         return render(request, 'users/register.html', {"form": form})

# message tags
# messages.debug
# messages.info
# messages.success
# messages.warning
# messages.error

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Your Account created! {username}")
            return redirect('blog')
    else:
        form = UserForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')