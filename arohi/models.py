from django.db import models


class User(models.Model):
    name = models.CharField(max_length=64)
    type = models.IntegerField()
    address = models.CharField(max_length=256)
    gender = models.CharField(max_length=16)


class Investor(User):
    region = models.CharField(max_length=64)
    category = models.CharField(max_length=64)
    investment_range_low = models.IntegerField()
    investment_range_hi = models.IntegerField()


class Entrepreneur(User):
    category = models.CharField(max_length=64)
    required_money = models.IntegerField()


class Consumer(User):
    pass


class Product(models.Model):
    name = models.CharField(max_length=64)
    category = models.CharField(max_length=64)
    description = models.CharField(max_length=256)
    price = models.IntegerField()
    producer = models.ForeignKey(Investor, on_delete=models.CASCADE)
    rating_sum = models.IntegerField()
    rating_cnt = models.IntegerField()

