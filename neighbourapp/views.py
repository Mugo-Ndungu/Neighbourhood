from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from .forms import *
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from .models import *


def home(request):
    estate = Neighbour.objects.all()
    return render(request, 'index.html', {"estate": estate})


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            profile = Profile(user=user)
            profile.save()
        return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'registration/register.html', locals())


def profile(request):
    profile = Profile.objects.filter(user=request.user)
    current_user = request.user
    neighbour = Neighbour.objects.filter(user=current_user)
    business = Business.objects.filter(user=current_user)
    image_form = ProfileForm()
    if request.method == 'POST':
        image_form = ProfileForm(
            request.POST, request.FILES, instance=request.user.profile)
        if image_form.is_valid:
            image_form.save()
        else:
            image_form = ProfileForm()
            return render(request, 'profile.html', locals())
    return render(request, 'profile.html', locals())


def create(request):
    area = Neighbour.objects.all()
    current_user = request.user
    if request.method == 'POST':
        form = NeighbourForm(request.POST, request.FILES)
        if form.is_valid():
            estate = form.save(commit=False)
            estate.user = current_user
            estate.save()
        return redirect('/')

    else:
        form = NeighbourForm()
    return render(request, 'create.html', locals())


def estate(request, id):
    businesses = Business.objects.filter(neighbourhood_id=id)
    post_form = PostForm()
    estate = Neighbour.objects.get(pk=id)
    posts = Post.objects.filter(neighbourhood_id=id)
    # posts = estate.post.all()
    return render(request, 'estate.html', locals())


def business(request):
    # business = Neighbour.objects.all()
    current_user = request.user
    if request.method == 'POST':
        form = BusinessForm(request.POST, request.FILES)
        if form.is_valid():
            business = form.save(commit=False)
            business.user = current_user
            business.save()
        return redirect('/')

    else:
        form = BusinessForm()
    return render(request, 'business.html', locals())


def post(request):
    neighbourhood = request.user.profile.neighbourhood
    if request.method == 'POST':
        post_form = PostForm(request.POST, request.FILES)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.user = request.user
            post.neighbourhood = neighbourhood
            post.save()

        return redirect('estate', neighbourhood.id)

    else:
        post_form = PostForm()
    return render(request, 'estate.html', locals())


def search_results(request):
    if 'name' in request.POST:
        search_term = request.POST.get("name")
        searched_business = Business.objects.filter(
            name__icontains=search_term)
        print('searched_business')
        message = f"{search_term}"

        return render(request, 'search.html', locals())

    else:
        message = "Please search for a valid business"
        return render(request, 'search.html', locals())


def profiles(request, id):
    profile = Profile.objects.get(user_id=id)
    business = Business.objects.filter(user_id=id)

    return render(request, 'profiles.html', locals())
