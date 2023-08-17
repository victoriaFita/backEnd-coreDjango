from django.db import models

from assistance.models import Equipment

class Assistance(models.Model):
    type = models.CharField(max_length=200)
    equipments = models.ForeignKey(Equipment, on_delete=models.PROTECT, related_name="assistances")

    def __str__(self):
        return self.type

    class Meta:
        verbose_name = "Assistance"
        verbose_name_plural = "Assistances"