from django.contrib import admin

from assistance.models import Equipment, Item, Assistance

admin.site.register(Assistance)
admin.site.register(Equipment)
admin.site.register(Item)
