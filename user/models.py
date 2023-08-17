import requests

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class User(AbstractUser):
    username = None
    email = models.EmailField(_("e-mail address"), unique=True)
    cpf = models.CharField(_("CPF"), max_length=11, blank=True, null=True)
    telefone = models.CharField(_("Phone"), max_length=11, blank=True, null=True)
    data_nascimento = models.DateField(
        _("Birth Date"), auto_now=False, auto_now_add=False, blank=True, null=True
    )
    cep = models.CharField(_("CEP"), max_length=8, blank=True, null=True)
    logradouro = models.CharField(_("Street"), max_length=200, blank=True, null=True)
    complemento = models.CharField(_("Complement"), max_length=200, blank=True, null=True)
    bairro = models.CharField(_("Neighborhood"), max_length=200, blank=True, null=True)
    localidade = models.CharField(_("City"), max_length=200, blank=True, null=True)
    uf = models.CharField(_("State"), max_length=2, blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    EMAIL_FIELD = "email"

    objects = CustomUserManager()

    def save(self, *args, **kwargs):
        if self.cep:
            url = f"https://viacep.com.br/ws/{self.cep}/json/"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                self.logradouro = data.get("logradouro")
                self.complemento = data.get("complemento")
                self.bairro = data.get("bairro")
                self.localidade = data.get("localidade")
                self.uf = data.get("uf")
        super().save(*args, **kwargs)
        

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        ordering = ["-date_joined"]
