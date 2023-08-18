from django.db import models

STATUS_EQUIPMENT = [
        ('new', 'Novo'),
        ('semi-new', 'Semi-novo'),
    ]

TYPE_EQUIPMENT = [
    ('athletic', "Athletic")
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

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Equipment"
        verbose_name_plural = "Equipments"