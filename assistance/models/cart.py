from django.db import models
from user.models import User
from assistance.models import Equipment, Item

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    equipment = models.ForeignKey(Equipment, on_delete=models.SET_NULL, null=True, blank=True)
    item = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.PositiveIntegerField(default=1)

    def clean(self):
        if not (self.equipment or self.item):
            raise ValidationError("CartItem must have either an Equipment or an Item.")
        if self.equipment and self.item:
            raise ValidationError("CartItem can't have both an Equipment and an Item.")
