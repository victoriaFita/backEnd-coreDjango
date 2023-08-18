from django.contrib import admin

from assistance.models import Equipment, Piece, Product, Assistance, CheckOut

admin.site.register(Assistance)
admin.site.register(CheckOut)
admin.site.register(Equipment)
admin.site.register(Piece)
admin.site.register(Product)
