from django.contrib import admin
from .models import account, cart, product
# Register your models here.

admin.site.register(account)
admin.site.register(product)
admin.site.register(cart)