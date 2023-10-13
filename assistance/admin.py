from django.contrib import admin

from assistance.models import Equipment, Item, Assistance, Cart, CartItem

admin.site.register(Assistance)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Equipment)
admin.site.register(Item)
