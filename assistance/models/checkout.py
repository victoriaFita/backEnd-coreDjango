from django.db import models

from assistance.models import Piece, Equipment, Assistance # change Piece to Item
from user.models import User

STATUS_CHOICES = [
        ('Pendente', 'Pendente'),
        ('Finalizado', 'Finalizado'),
    ]

class CheckOut(models.Model):
    description = models.CharField(max_length=200) # remove it because there's no sense having a description for a checkout
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="checkouts")
    items = models.ForeignKey(Piece, on_delete=models.PROTECT, related_name="checkouts", null=True, blank=True) # change Piece to Item
    equipments = models.ForeignKey(Equipment, on_delete=models.PROTECT, related_name="checkouts", null=True, blank=True)
    assistances = models.ForeignKey(Assistance, on_delete=models.PROTECT, related_name="checkouts", null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pendente')

    def __str__(self):
        return self.description
    
    class Meta:
        verbose_name = "CheckOut"
        verbose_name_plural = "CheckOuts"
