from django.db import models


class User(models.Model):
    name = models.CharField(max_length=64)
    type = models.CharField(max_length=32)
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


class Investor(User):
    region = models.CharField(max_length=64)
    category_preference = models.TextField()
    investment_range_low = models.IntegerField()
    investment_range_hi = models.IntegerField()


class Entrepreneur(User):
    product_category = models.CharField(max_length=64)
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
                product_category='silk'
            )
            user.save()


class Consumer(User):
    category_preference = models.TextField()


class Product(models.Model):
    Producer = models.ForeignKey(Entrepreneur, on_delete=models.CASCADE)
    cost_per_unit = models.IntegerField()
    funded_units = models.IntegerField()
    sales_goal = models.IntegerField()

    name = models.CharField(max_length=64)
    price = models.IntegerField()
    category = models.CharField(max_length=32)
    sold = models.IntegerField()
    quantity = models.IntegerField()
    discount = models.IntegerField()
    rating = models.FloatField()
    reviews = models.IntegerField()

    @staticmethod
    def generate_fake(count=100):
        from random import seed, randint
        import forgery_py

        seed()

        for i in range(count):
            product = Product(
                Producer=Entrepreneur.objects.filter(id=randint(100, 130)),
                name=forgery_py.name.industry(),
                sales_goal=(randint(10, 50)/10),
                cost_per_unit=(randint(10, 50)/10),
                funded_units=(randint(10, 50)/10),
                rating=(randint(10, 50)/10),
                reviews=randint(15, 100),
                price=randint(300, 5000),
                sold=randint(15, 50),
                quantity=randint(50, 100),
                discount=randint(1, 50),
                category='loom'
            )
            product.save()


class Investment(models.Model):
    Product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    Investor = models.ForeignKey(Investor, on_delete=models.CASCADE)
    amount = models.IntegerField()
    date = models.DateField()
    margin = models.IntegerField()
    units = models.IntegerField()

    @staticmethod
    def generate_fake(count=100):
        from random import seed, randint
        import forgery_py

        seed()

        for i in range(count):
            investment = Investment(
                Investor=Investor.objects.first(),
                Product_id=randint(1, 30),
                amount=randint(5000, 15000),
                margin=randint(5, 40),
                units=randint(40, 200),
                date=forgery_py.date.date()
            )
            investment.save()


class Order(models.Model):
    Buyer = models.ForeignKey(Consumer, on_delete=models.CASCADE)
    Product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    is_delivered = models.BooleanField()
    expected_delivery_date = models.DateField()

    @staticmethod
    def generate_fake(count=100):
        from random import seed, randint
        import forgery_py

        seed()

        for i in range(count):
            order = Order(
                Buyer_id=1,
                Product_id=randint(1, 20),
                quantity=randint(10, 50),
                is_delivered=randint(0, 1),
                expected_delivery_date=forgery_py.date.date()
            )
            order.save()
