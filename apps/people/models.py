import uuid
from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from apps.core.helpers.multiple_choices import (SCHOLARITY, TIME, BOOLEAN_TYPE,
                                                UF, GENDER, CIVIL_STATUS,
                                                EMPLOYEES_TYPE)
from apps.accounts.models import User


def generate_uuid(value):
    return ''.join(str(value).split('-'))


class Information(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(editable=False)
    modification_date = models.DateTimeField()

    def save(self, *args, **kwargs):
        if not self.creation_date:
            self.creation_date = timezone.now()
        self.modification_date = timezone.now()
        return super(Information, self).save(*args, **kwargs)


class Person(Information):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.IntegerField(choices=GENDER, default=0)
    civil_status = models.IntegerField(choices=CIVIL_STATUS, default=0)
    mothers_name = models.CharField(max_length=60)
    fathers_name = models.CharField(max_length=60, blank=True)
    occupation = models.CharField(max_length=40)
    rg = models.CharField(unique=True, max_length=12)
    cpf = models.CharField(unique=True, max_length=14)
    email = models.EmailField(max_length=60)
    home_phone = models.CharField(max_length=16, null=True, blank=True)
    cellphone = models.CharField(max_length=16, null=True, blank=True)
    address = models.CharField(max_length=100)
    number = models.IntegerField()
    complement = models.CharField(max_length=80, null=True, blank=True)
    neighborhood = models.CharField(max_length=40)
    city = models.CharField(max_length=40)
    country = models.CharField(max_length=32)
    uf = models.CharField(max_length=2, choices=UF, default=0)
    cep = models.CharField(max_length=10, blank=True)
    comments = models.CharField(max_length=1024, blank=True, null=True)
    ref_person = models.CharField(max_length=50, default='ref')
    slug = models.SlugField(max_length=150, unique=True, default='page-slug')

    @property
    def full_name(self):
        return f'{self.name} {self.last_name}'

    @property
    def complete_address(self):
        return f'{self.address}, {self.number} - {self.neighborhood} {self.city}/{self.uf}'


class Students(Person):
    scholarity = models.IntegerField(choices=SCHOLARITY, default=0)
    school = models.CharField(max_length=100)
    time = models.IntegerField(choices=TIME, default=0)

    def __str__(self):
        return f'{self.name} {self.last_name}'

    def save(self, *args, **kwargs):
        self.ref_person = f'{slugify(self.name)}-{slugify(self.last_name)}'
        if not self.id:
            self.slug = generate_uuid(uuid.uuid4())

        super(Students, self).save(*args, **kwargs)

    class Meta:
        ordering = ['name']
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'


class Donors(Person):
    def __str__(self):
        return f'{self.name} {self.last_name}'

    def save(self, *args, **kwargs):
        self.ref_person = f'{slugify(self.name)}-{slugify(self.last_name)}'
        if not self.id:
            self.slug = generate_uuid(uuid.uuid4())

        super(Donors, self).save(*args, **kwargs)

    class Meta:
        ordering = ['name']
        verbose_name = 'Doador'
        verbose_name_plural = 'Doadores'


class Employees(Person):
    baghelped = models.IntegerField(choices=BOOLEAN_TYPE, default=0)
    salary = models.CharField(max_length=20, default=0)
    employeestype = models.IntegerField(choices=EMPLOYEES_TYPE, default=0)

    def __str__(self):
        return f'{self.name} {self.last_name}'

    def save(self, *args, **kwargs):
        self.ref_person = f'{slugify(self.name)}-{slugify(self.last_name)}'
        if not self.id:
            self.slug = generate_uuid(uuid.uuid4())

        super(Employees, self).save(*args, **kwargs)

    class Meta:
        ordering = ['name']
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'
