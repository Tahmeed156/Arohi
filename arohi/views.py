from .models import Product, Entrepreneur
from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import Http404
from arohi.models import *


def home(request):
    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html')


def login(request):
    return render(request, 'auth/login.html')


def sign_up(request):
    return render(request, 'auth/signup.html')


def consumer_feed(request, page=1):
    try:
        product_list = Product.objects.all()
    except Product.DoesNotExist:
        raise Http404("Products does not exist.")

    # Shows 20 buyers per page
    pag = Paginator(product_list, 20)
    products = pag.get_page(page)
    return render(request, 'feed/consumer_feed.html', {'product_list': products, 'pagination': pag,
                                                       'page': page})


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


def dashboard_entrepreneur(request):
    return render(request, 'dashboard/entrepreneur.html')


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


def dashboard_investor(request):
    # Hard coded for sample
    user = Investor.objects.first()
    investments = Investment.objects.filter(Investor=user).all()
    context = {
        'investments': investments,
    }
    return render(request, 'dashboard/investor.html', context=context)


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
