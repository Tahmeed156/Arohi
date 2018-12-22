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
    # producer = models.ForeignKey(, on_delete=models.CASCADE)
    rating_sum = models.IntegerField()
    rating_cnt = models.IntegerField()

    @staticmethod
    def generate_fake(count=100):
        from random import seed, randint
        import forgery_py

        seed()

        for i in range(count):
            product = Product(
                name=forgery_py.name.industry(),
                category=forgery_py.lorem_ipsum.words(randint(3, 5)),
                description=forgery_py.lorem_ipsum.words(randint(5, 15)),
                price=(randint(1, 100)),
                # producer_id=1,
                rating_sum=(randint(50, 100)),
                rating_cnt=(randint(15, 30)),
            )
            product.save()

