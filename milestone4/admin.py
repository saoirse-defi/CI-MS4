from django.contrib import admin
from .models import Buyer, Seller, Listing, Sale, Rating

# Register your models here.
admin.site.register(Buyer)
admin.site.register(Seller)
admin.site.register(Listing)
admin.site.register(Sale)
admin.site.register(Rating)
