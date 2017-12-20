from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from django.contrib.auth import authenticate, login
from django.views import generic
from django.views.generic import View
from django.views.decorators.http import require_POST
from .cart import Cart
from .forms import CartClothAddForm, CartShoeAddForm, CheckOutForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from decimal import Decimal as D
from rest_framework import generics
from .serializers import ProductSerializer
from .serializers import UserSerializer
from django.contrib.auth.models import User

# Create your views here.
def product_list(request):
    cart_cloth_form = CartClothAddForm(auto_id=False)
    cart_shoe_form = CartShoeAddForm(auto_id=False)
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products, 'cloth_form': cart_cloth_form, 'shoe_form': cart_shoe_form,})

def menclothes(request):
    cart_cloth_form = CartClothAddForm(auto_id=False)
    products = Product.objects.all()
    return render(request, 'products/menClothes.html', {'products': products, 'cloth_form': cart_cloth_form,})

def menshoes(request):
    cart_shoe_form = CartShoeAddForm(auto_id=False)
    products = Product.objects.all()
    return render(request, 'products/menShoes.html', {'products': products, 'shoe_form': cart_shoe_form,})

def womenclothes(request):
    cart_cloth_form = CartClothAddForm(auto_id=False)
    products = Product.objects.all()
    return render(request, 'products/womenClothes.html', {'products': products, 'cloth_form': cart_cloth_form,})

def womenshoes(request):
    cart_shoe_form = CartShoeAddForm(auto_id=False)
    products = Product.objects.all()
    return render(request, 'products/womenShoes.html', {'products': products, 'shoe_form': cart_shoe_form,})

def shoppingcart(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_cloth_form'] = CartClothAddForm(initial={'size':item['size'], 'quantity': item['quantity'], 'update': True}, auto_id=False)
        item['update_quantity_shoe_form'] = CartShoeAddForm(initial={ 'quantity': item['quantity'], 'size':item['size'], 'update': True}, auto_id=False)
    products = Product.objects.all()
    return render(request, 'products/shoppingCart.html', {'products': products, 'cart': cart})

class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@csrf_protect
def price_filter_product_list(request):
    if (request.GET.get('mybtn')):
        price1 = request.GET.get('min_price')
        price2 = request.GET.get('max_price')
        if price1 =='':
            price1=0
        if price2=='':
            price2=999

        my_product = Product.objects.filter(price__range=(price1, price2))
        cart_cloth_form = CartClothAddForm()
        cart_shoe_form = CartShoeAddForm()
    return render(request,"products/product_list.html", {'products': my_product, 'cloth_form': cart_cloth_form, 'shoe_form': cart_shoe_form})

@csrf_protect
def price_filter_woman_shoes(request):
    if (request.GET.get('mybtn')):
        price1 = request.GET.get('min_price')
        price2 = request.GET.get('max_price')
        if price1 =='':
            price1=0
        if price2=='':
            price2=999

        my_product = Product.objects.filter(price__range=(price1, price2))
        cart_shoe_form = CartShoeAddForm()
    return render(request,"products/womenShoes.html", {'products': my_product, 'shoe_form': cart_shoe_form})

@csrf_protect
def price_filter_woman_clothes(request):
    if (request.GET.get('mybtn')):
        price1 = request.GET.get('min_price')
        price2 = request.GET.get('max_price')
        if price1 =='':
            price1=0
        if price2=='':
            price2=999

        my_product = Product.objects.filter(price__range=(price1, price2))
        cart_cloth_form = CartClothAddForm()
    return render(request,"products/womenClothes.html", {'products': my_product, 'cloth_form': cart_cloth_form})

@csrf_protect
def price_filter__men_clothes(request):
    if (request.GET.get('mybtn')):
        price1 = request.GET.get('min_price')
        price2 = request.GET.get('max_price')
        if price1 =='':
            price1=0
        if price2=='':
            price2=999

        my_product = Product.objects.filter(price__range=(price1, price2))
        cart_cloth_form = CartClothAddForm()
    return render(request,"products/menClothes.html", {'products': my_product, 'cloth_form': cart_cloth_form})

@csrf_protect
def price_filter_men_shoes(request):
    if (request.GET.get('mybtn')):
        price1 = request.GET.get('min_price')
        price2 = request.GET.get('max_price')
        if price1 =='':
            price1=0
        if price2=='':
            price2=999

        my_product = Product.objects.filter(price__range=(price1, price2))
        cart_shoe_form = CartShoeAddForm()
    return render(request,"products/menShoes.html", {'products': my_product, 'shoe_form': cart_shoe_form})


@login_required
def checkout(request):
    cart = Cart(request)
    form = CheckOutForm()
    return render(request, 'products/checkout.html', {'cart': cart, 'form':form})

def checkoutnext(request):
    cart = Cart(request)
    form = CheckOutForm(request.POST)
    if form.is_valid():
        cart.clear()
        messages.info(request, 'Thank you for your order!')
    return redirect('products:home')


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    if product.clothingtype == "CLOTHING":
        form = CartClothAddForm(request.POST)
    elif product.clothingtype == "SHOE":
        form = CartShoeAddForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 size=cd['size'],
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
        if cd['update']:
            messages.info(request, 'Your shoppingcart has been updated')
        else:
            messages.info(request, 'Product has been added to your shopping cart.')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('products:shoppingcart')
