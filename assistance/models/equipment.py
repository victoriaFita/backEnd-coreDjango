from django.db import models

from uploader.models import Image

class Equipment(models.Model):
    name = models.CharField(max_length=200)
    model = models.CharField(max_length=200, null=True, blank=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    cover = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None,
    )
    is_on_promotion = models.BooleanField(default=False, verbose_name="Em Promoção")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Equipment"
        verbose_name_plural = "Equipments"
