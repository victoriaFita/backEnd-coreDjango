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

class Piece(models.Model):
    name = models.CharField(max_length=200)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    manufacture_date = models.DateField()
    last_maintenance_date = models.DateField()
    status = models.CharField(max_length=200)  # Status of the part (e.g., "Working", "In Repair", etc.)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_in_stock = models.IntegerField()
    category = models.CharField(max_length=200)  # Category of the product (e.g., "Cleaning", "Repair", etc.)

    def __str__(self):
        return self.name
