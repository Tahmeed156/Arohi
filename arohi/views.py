from .models import Product, Entrepreneur
from django.shortcuts import render
from django.http import Http404


def login(request):
    return render(request, 'templates/auth/login.html')


def consumer_feed(request):
    try:
        product_list = Product.objects.all()
    except Product.DoesNotExist:
        raise Http404("Products does not exist.")

    return render(request, 'templates/feed/consumer.html', {'product_list': product_list})


def investor_feed(request):
    try:
        entrepreneur_list = Entrepreneur.objects.all()
    except Entrepreneur.DoesNotExist:
        raise Http404("Entrepreneurs don't exist in the database.")

    return render(request, 'templates/feed/entrepreneur.html', {'entrepreneur_list':entrepreneur_list})

