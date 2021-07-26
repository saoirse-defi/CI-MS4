from django.db import models


# Create your models here.


# Seller, Buyer inherit from User class
# which in turn inherits from Django's base Model class

class User(models.Model):
    username = models.CharField(max_length=50, null=False, blank=False)
    email = models.CharField(max_length=75, null=False, blank=False)
    town = models.CharField(max_length=20, null=False, blank=False)
    county = models.CharField(max_length=20, null=False, blank=False)
    join_date = models.DateField()

    def __str__(self):
        return self.username


class Seller(User):
    # rating out of 5, 1 decimal place
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    sales = models.IntegerField()


class Buyer(User):
    purchases = models.IntegerField()


class Listing(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    seller_id = models.ForeignKey(Seller, on_delete=models.CASCADE)
    description = models.CharField(max_length=200, null=False, blank=False)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    weight = models.DecimalField(max_digits=4, decimal_places=2)
    quantity = models.IntegerField()

    def __str__(self):
        return self.name


# Rating needs sale, so inheritance has been used

class Sale(models.Model):
    sale_date = models.DateField()
    listing_id = models.ForeignKey(Listing, on_delete=models.CASCADE)
    seller_id = models.ForeignKey(Seller, on_delete=models.CASCADE)
    buyer_id = models.ForeignKey(Buyer, on_delete=models.CASCADE)

    def __str__(self):
        return self.sale_date


class Rating(Sale):
    rating_date = models.DateField()
    score = models.IntegerField()

    def __str__(self):
        return self.rating_date
