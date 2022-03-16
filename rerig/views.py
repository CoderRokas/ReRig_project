from unicodedata import category
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.models import User

from rerig.forms import UserForm,PostForm
from rerig.models import Post,Review

def index(request):
    context_dict = {}

    post_list = Post.objects.order_by('-averageRating')[:5]

    context_dict['posts'] = post_list
    
    return render(request, 'rerig/index.html', context=context_dict)


def about(request):
    context_dict = {}
    return render(request, 'rerig/about.html', context=context_dict)

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('rerig:index'))
            else:
                return HttpResponse("Your Rango account is disabled")
        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied")
    else:
        return render(request, 'rerig/login.html')

def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(request.POST)

        if user_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()
    
    return render(request, 'rerig/register.html', context={'user_form':user_form, 'registered':registered})

@login_required
def account(request, username_slug):
    return render(request, 'rerig/account.html')

def search(request):
    context_dict={}

    post_list = Post.objects.order_by('-date')

    context_dict['posts'] = post_list

    return render(request, 'rerig/search.html', context=context_dict)

@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('rerig:index'))

def show_post(request):
    return(request, 'rerig/post.html')

@login_required
def add_post(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST, request.FILES)
        if post_form.is_valid():
            titleInput = post_form.cleaned_data.get("title")
            descriptionInput = post_form.cleaned_data.get("descirption")
            imageInput = post_form.cleaned_data.get("image")
            obj = Post.objects.create(
                author = User.username,
                title = titleInput,
                description = descriptionInput,
                image = imageInput,
                )
            obj.save()
            return render(request , 'rerig/post.html')
        else:
            print(post_form.errors)
    else:
        post_form = PostForm()
    
    context_dict = {'post_form': post_form}
    return render (request, 'rerig/add_post.html', context=context_dict)

# Create your views here.
