from django.db import models

from assistance.models import Equipment

class Piece(models.Model):
    name = models.CharField(max_length=200)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    manufacture_date = models.DateField()
    last_maintenance_date = models.DateField()
    status = models.CharField(max_length=200)  # Status of the part (e.g., "Working", "In Repair", etc.)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Piece"
        verbose_name_plural = "Pieces"
