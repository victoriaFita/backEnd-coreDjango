from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=200)  # Category of the service (e.g., "Cleaning", "Repair", etc.)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"