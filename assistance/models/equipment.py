from django.db import models

class Equipment(models.Model):
    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    manufacture_date = models.DateField()
    last_maintenance_date = models.DateField()
    location = models.CharField(max_length=200)  # Where the equipment is located
    status = models.CharField(max_length=200)  # Status of the equipment (e.g., "Working", "In Repair", etc.)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Equipment"
        verbose_name_plural = "Equipments"