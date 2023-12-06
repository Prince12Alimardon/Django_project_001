from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, About
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .form import UserForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required


# Create your views here.

# @login_required
def index(request):
    post = Post.objects.all().order_by('-id')[:3]
    return render(request, 'blog.html', {'posts': post})


@login_required
def detail_view(request, pk):
    post = get_object_or_404(Post, id=pk)
    return render(request, 'detail.html', {'posts': post})


def about(requset):
    object = About.objects.all().order_by('-id')[:1]
    context = {
        'abouts': object
    }
    return render(requset, 'about.html', context)


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


def u_profile(request):
    if request.method == 'POST':
        user_update_form = UserUpdateForm(request.POST, instance=request.user)
        profile_update_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_update_form.is_valid() and profile_update_form.is_valid():
            user_update_form.save()
            profile_update_form.save()
            messages.success(request, f"Accountingiz yangilandi")
            return redirect('profile')
    else:
        user_update_form = UserUpdateForm(instance=request.user)
        profile_update_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': user_update_form,
        'p_form': profile_update_form,
    }
    return render(request, 'users/profile_update.html', context)
