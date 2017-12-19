from products.models import Product
from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth import authenticate, login
from django.views import generic
from django.views.generic import View
from products.forms import UserForm, ProfileForm, SignUpForm
from products.cart import Cart
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import transaction

# Create your views here.
def homepage(request):
    cart = Cart(request)
    return render(request, 'homepage.html', {'cart': cart})

def menclothes(request):
    products = Product.objects.all()
    return render(request, 'products/menclothes.html', {'products': products})

def menshoes(request):
    products = Product.objects.all()
    return render(request, 'products/menshoes.html', {'products': products})

def womenclothes(request):
    products = Product.objects.all()
    return render(request, 'products/womenclothes.html', {'products': products})

def womenshoes(request):
    products = Product.objects.all()
    return render(request, 'products/womenshoes.html', {'products': products})

def shoppingcart(request):
    products = Product.objects.all()
    return render(request, 'products/shoppingcart.html', {'products': products})

def base(request):
    return render_to_response('base_layout.html', context_instance=RequestContext(request))

def template(request):
    return render_to_response('template_no_pr.html', context_instance=RequestContext(request))

def profile(request):
    return render_to_response('registration/profile.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.city = form.cleaned_data.get('city')
            user.profile.adress = form.cleaned_data.get('adress')
            user.profile.ZIP_code = form.cleaned_data.get('ZIP_code')
            user.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('products:home')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'registration/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
