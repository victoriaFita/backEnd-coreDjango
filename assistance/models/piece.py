from django.db import models

from uploader.models import Image

from assistance.models import Equipment

class Piece(models.Model):
    name = models.CharField(max_length=200)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    manufacture_date = models.DateField()
    last_maintenance_date = models.DateField()
    status = models.CharField(max_length=200) 
    image =  models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None,
    )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Piece"
        verbose_name_plural = "Pieces"
