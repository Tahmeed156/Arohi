from .models import Product, Entrepreneur
from django.shortcuts import render
from django.http import Http404


# def login(request):
#     return render(request, 'auth/login.html')


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

