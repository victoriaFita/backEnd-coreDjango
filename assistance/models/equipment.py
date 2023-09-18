from django.db import models

from uploader.models import Image

STATUS_EQUIPMENT = [
        ('new', 'Novo'),
        ('semi-new', 'Semi-novo'),
    ]

TYPE_EQUIPMENT = [
    ('athletic', "Athletic"),
    ('supergold', "SuperGold")
]

class Equipment(models.Model):
    name = models.CharField(max_length=200) # remove it
    model = models.CharField(max_length=200)
    brand = models.CharField(max_length=200, choices=TYPE_EQUIPMENT, default='athletic') #
    manufacture_date = models.DateField() # remove it
    last_maintenance_date = models.DateField() # remove it
    location = models.CharField(max_length=200)  # remove it
    status = models.CharField(max_length=20, choices=STATUS_EQUIPMENT) # change it to condition
    description = models.CharField(max_length=200, blank=True, null=True) 
    image = models.ForeignKey(
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
        verbose_name = "Equipment"
        verbose_name_plural = "Equipments"