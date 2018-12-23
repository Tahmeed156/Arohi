from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import Http404
from arohi.models import *
from django import forms
from django.http import HttpResponse


def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        next = request.GET.get('next')
        user = authenticate(request, username=username, password=password)
        print(user.username)
        if user:
            login(request, user)
            if next:
                return redirect(next)
            else:
                messages.success(request, "You have successfully logged in!")
                return redirect('arohi:feed')
        else:
            messages.error(request, "Provide valid credentials.")
            return render(request, 'auth/login.html')
    else:
        return render(request, 'auth/login.html')


@login_required
def user_logout(request):
    messages.success(request, "You have been logged out!")
    logout(request)
    return redirect('arohi:login')


def home(request):
    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html')


def sign_up(request):
    return render(request, 'auth/signup.html')


@login_required
def feed(request, page=1):
    if request.user.username == 'consumer' or request.user.username == 'entrepreneur':
        return consumer_feed(request, page=page)
    elif request.user.username == 'investor':
        return investor_feed(request, page=page)


@login_required
def consumer_feed(request, page=1):
    print(request.user.username)
    try:
        product_list = Product.objects.all()
    except Product.DoesNotExist:
        raise Http404("Products does not exist.")

    # Shows 20 buyers per page
    pag = Paginator(product_list, 20)
    products = pag.get_page(page)
    return render(request, 'feed/consumer_feed.html', {'product_list': products, 'pagination': pag,
                                                       'page': page})


@login_required
def investor_feed(request, page=1):
    try:
        entrepreneur_list = Entrepreneur.objects.all()
    except Entrepreneur.DoesNotExist:
        raise Http404("Entrepreneurs don't exist in the database.")

    # Shows 20 buyers per page
    pag = Paginator(entrepreneur_list, 20)
    entrepreneurs = pag.get_page(page)
    return render(request, 'feed/investor_feed.html', {'entrepreneur_list': entrepreneurs, 'pagination': pag,
                                                       'page': page})


@login_required
def dashboard(request):
    if request.user.username == 'consumer':
        return dashboard_consumer(request)
    elif request.user.username == 'investor':
        return dashboard_investor(request)
    elif request.user.username == 'entrepreneur':
        return dashboard_entrepreneur(request)


@login_required
def dashboard_entrepreneur(request):
    user = Entrepreneur.objects.filter(id=114).first()
    context = {
        'products': Product.objects.filter(Producer=user).all()
    }
    return render(request, 'dashboard/entrepreneur.html', context=context)


@login_required
def dashboard_consumer(request):
    # Hard coded for sample
    user = Consumer.objects.first()
    products = Order.objects.filter(Buyer=user).order_by('expected_delivery_date').all()
    context = {
        'latest_delivery_date': products.first().expected_delivery_date,
        'bought_products': products.filter(is_delivered=False).all(),
        'delivered_products': products.filter(is_delivered=True).all()
    }
    return render(request, 'dashboard/consumer.html', context=context)


@login_required
def dashboard_investor(request):
    # Hard coded for sample
    user = Investor.objects.first()
    investments = Investment.objects.filter(Investor=user).all()
    context = {
        'investments': investments,
    }
    return render(request, 'dashboard/investor.html', context=context)


@login_required
def profile_entrepreneur(request):
    return render(request, 'profiles/entrepreneur.html')


@login_required
def profile_consumer(request):
    return render(request, 'profiles/consumer.html')


@login_required
def profile_investor(request):
    return render(request, 'profiles/investor.html')


@login_required
def add_product(request):
    return render(request, 'product/add.html')


@login_required
def buy_product(request):
    return render(request, 'product/buy.html')


class ContactForm(forms.Form):
    name = forms.CharField(max_length=64, required=True)
    email = forms.EmailField(max_length=64, required=True)
    messages = forms.CharField(widget=forms.Textarea)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            return HttpResponse("Thanks for contacting us!")
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})
