from django.db import models
from django.urls import reverse

from core.helpers.multiple_choices import (SCHOLARITY, TIME, BOOLEAN_TYPE,
                                           GENDER, CIVIL_STATUS, UF, NI,
                                           EMPLOYEES_TYPE)


class Person(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.BooleanField(choices=GENDER, max_length=14)
    civil_status = models.IntegerField(choices=CIVIL_STATUS, max_length=13)
    mothers_name = models.CharField(max_length=60)
    fathers_name = models.CharField(max_length=60, blank=True, default=NI)
    occupation = models.CharField(max_length=40)
    rg = models.CharField(unique=True, max_length=9)
    cpf = models.CharField(unique=True, max_length=11)
    email = models.EmailField(max_length=60)
    home_phone = models.CharField(max_length=10, null=True, blank=True, default=NI)
    cell_phone = models.CharField(max_length=10, null=True, blank=True, default=NI)
    address = models.CharField(max_length=100)
    number = models.IntegerField(max_length=4)
    complement = models.CharField(max_length=80, null=True, blank=True)
    neighborhood = models.CharField(max_length=40)
    city = models.CharField(max_length=40)
    country = models.CharField(max_length=32)
    uf = models.CharField(max_length=2, choices=UF)
    cep = models.CharField(max_length=10, blank=True, default=NI)
    comments = models.CharField(max_length=1024, blank=True, null=True)

    @property
    def full_name(self):
        return f'{self.name} {self.last_name}'

    @property
    def complete_address(self):
        return f'{self.address}, {self.number} - {self.neighborhood} {self.city}/{self.uf}'
