from django.db import models
from django.db.models import CharField, ForeignKey, URLField, CASCADE, DateTimeField, Sum, EmailField, PositiveIntegerField
from django.utils.translation import ugettext_lazy as _
# Create your models here.
from django.contrib.auth.models import User
# Category: title
class Category(models.Model):
    title = models.CharField(max_length = 100)
    def __str__(self):
        return self.title

# http://stackoverflow.com/questions/10052220/advantages-to-using-urlfield-over-textfield#comment49011703_10052288
# Product: title, image, description, price (both value and currency), category, likes (user likes product and it gets added to user's wish list);	
class Product(models.Model):
	title = models.CharField(max_length = 100)
	description = models.CharField(max_length = 500)
	

	image = URLField(max_length=2000)
	price = models.CharField(max_length = 10)
	currency = models.CharField(max_length = 5)

	category = ForeignKey(
        Category,
        on_delete=CASCADE,
    )

	likes = models.PositiveIntegerField(default=0)

    # def __str__(self):
    #     return self.title

# Type of deliveries: title, price (could be fixed value or percent of product's price)
#could be fixed value or percent of product's price
class DeliveryType(models.Model):
    title = models.CharField(max_length = 100)
    price = models.CharField(max_length = 10)
    fixed = models.BooleanField(default = True)

    def __str__(self):
        return self.title
# Order: product (which is ordered), user (who orders), chosen delivery, total price (product's price + delivery's price), count of products;
class Order(models.Model):

    user = ForeignKey(
        User,
        on_delete=CASCADE,
    )

    delivery = ForeignKey(
        DeliveryType,
        on_delete=CASCADE,
    )

    product = ForeignKey(
        Product,
        on_delete=CASCADE,
    )
	#total price (product's price + delivery's price)
    total_price = models.CharField(max_length = 20)
    product_count = models.PositiveIntegerField(default=0)
    

class Like(models.Model):
    user = ForeignKey(
        User,
        on_delete=CASCADE,
    )

    product = ForeignKey(
        Product,
        on_delete=CASCADE,
    )