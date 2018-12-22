from django.db import models


class User(models.Model):
    name = models.CharField(max_length=64)
    type = models.IntegerField()
    address = models.CharField(max_length=256)
    gender = models.CharField(max_length=16)

    @staticmethod
    def generate_fake(count=100):
        from random import seed, randint
        import forgery_py

        seed()

        for i in range(count):
            user = User(
                name=forgery_py.name.full_name(),
                type=0,
                gender='female',
                address=forgery_py.address.state(),
            )
            user.save()

    class Meta:
        abstract: True


class Investor(User):
    region = models.CharField(max_length=64)
    category = models.CharField(max_length=64)
    investment_range_low = models.IntegerField()
    investment_range_hi = models.IntegerField()


class Entrepreneur(User):
    category = models.CharField(max_length=64)
    required_money = models.IntegerField()

    @staticmethod
    def generate_fake(count=100):
        from random import seed, randint
        import forgery_py

        seed()

        for i in range(count):
            user = Entrepreneur(
                # User=User.objects.get(id=randint(1, 50)),
                name=forgery_py.name.full_name(),
                type=0,
                gender='female',
                address=forgery_py.address.state(),
                required_money=(randint(5000, 15000)),
                category='loom'
            )
            user.save()


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


class Order(models.Model):
    buyer = models.ForeignKey(Consumer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    is_delivered = models.BooleanField()
    expected_delivery_date = models.DateField()
