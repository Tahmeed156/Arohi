from .models import Product, Entrepreneur
from django.shortcuts import render
from django.http import Http404


def home(request):
    render(request, 'index.html')


def login(request):
    return render(request, 'auth/login.html')


def sign_up(request):
    return render(request, 'auth/signup.html')


def consumer_feed(request):
    try:
        product_list = Product.objects.all()
    except Product.DoesNotExist:
        raise Http404("Products does not exist.")

    return render(request, 'feed/consumer_feed.html', {'product_list': product_list})


def investor_feed(request):
    try:
        entrepreneur_list = Entrepreneur.objects.all()
    except Entrepreneur.DoesNotExist:
        raise Http404("Entrepreneurs don't exist in the database.")

    return render(request, 'feed/investor_feed.html', {'entrepreneur_list': entrepreneur_list})


def dashboard_entrepreneur(request):
    return render(request, 'dashboard/entrepreneur.html')


def dashboard_consumer(request):
    return render(request, 'dashboard/consumer.html')


def dashboard_investor(request):
    return render(request, 'dashboard/investor.html')


def profile_entrepreneur(request):
    return render(request, 'profiles/entrepreneur.html')


def profile_consumer(request):
    return render(request, 'profiles/consumer.html')


def profile_investor(request):
    return render(request, 'profiles/investor.html')


def add_product(request):
    return render(request, 'product/add.html')


def buy_product(request):
    return render(request, 'product/buy.html')
