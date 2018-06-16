import uuid
from django.db import models
from django.utils.text import slugify
from apps.people.models import Donors, Employees, Information, Students
from apps.core.helpers.multiple_choices import (DONATIONS_TYPE, EXPENSES_TYPE,
                                                STATUS_MP, TIME, UNIT_TYPE)
from apps.people.models import generate_uuid, Information


class AdmInformation(Information):
    ref_adm = models.CharField(max_length=50, default='ref')
    slug = models.SlugField(max_length=150, unique=True, default='page-slug')


class Courses(AdmInformation):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    students_number = models.IntegerField(default=0)
    duration = models.CharField(max_length=20)

    def save(self, *args, **kwargs):
        self.ref_adm = f'{slugify(self.name)}'
        if not self.id:
            self.slug = generate_uuid(uuid.uuid4())

        super(Courses, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ['name']
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'


# class Classes(Information):
#     course = models.ForeignKey(Courses, on_delete=models.CASCADE)
#     name = models.CharField(max_length=50)
#     employees = models.ForeignKey(Employees, on_delete=models.CASCADE)
#     opening_time = models.CharField(max_length=5)
#     final_time = models.CharField(max_length=5)
#     time = models.CharField(choices=TIME, max_length=100)
#     days_of_the_week = models.CharField(max_length=50)
#     students = models.ForeignKey('adm.StudentClasses', null=True, blank=True,
#                                  on_delete=models.CASCADE)
#
#     def __str__(self):
#         return str(self.name)
#
#     class Meta:
#         ordering = ['name']
#         verbose_name = 'Turma'
#         verbose_name_plural = 'Turmas'
#
#
# class Enrollment(Information):
#     student = models.ForeignKey(Students, on_delete=models.CASCADE)
#     course = models.ForeignKey(Courses, on_delete=models.CASCADE)
#     student_class = models.ForeignKey(Classes, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return f'{self.pk} - {self.student.full_name}'
#
#     class Meta:
#         ordering = ['pk']
#         verbose_name = 'Matrícula'
#         verbose_name_plural = 'Matrículas'
#
#
# class MonthlyPayment(Information):
#     enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE)
#     value = models.DecimalField(max_digits=6, decimal_places=2, default=0)
#     due_date = models.DateField(null=True, blank=True)
#     payday = models.DateField(null=True, blank=True)
#     status = models.CharField(max_length=3, choices=STATUS_MP, default=0)
#
#     def __str__(self):
#         return str(self.enrollment.student.name)
#
#     class Meta:
#         ordering = ['pk']
#         verbose_name = 'Mensalidade'
#         verbose_name_plural = 'Mensalidades'
#
#
# class StudentClasses(Information):
#     classes_id = models.ForeignKey(Classes, null=True, blank=True,
#                                    on_delete=models.CASCADE)
#     student = models.ForeignKey(Students, null=True, blank=True,
#                                 on_delete=models.CASCADE)
#
#     def __str__(self):
#         return str(self.student)
#
#     class Meta:
#         ordering = ['student']
#         verbose_name = 'Estudante por turma'
#         verbose_name_plural = 'Estudantes por turmas'
#
#
# class Donations(Information):
#     service_type = models.CharField('Tipo de serviço', max_length=12,
#                                     choices=DONATIONS_TYPE,
#                                     default='Recebimento')
#     donor = models.ForeignKey(Donors, verbose_name='Doador',
#                               on_delete=models.CASCADE)
#     item = models.CharField(max_length=100, default='')
#     description = models.TextField(blank=True)
#     quantity = models.PositiveSmallIntegerField(default=0)
#     date = models.DateField(null=True, blank=True)
#
#     def __str__(self):
#         return str(self.service_type)
#
#     class Meta:
#         ordering = ['service_type']
#         verbose_name = 'Doação'
#         verbose_name_plural = 'Doações'
#
#
# class Expenses(Information):
#     service_type = models.CharField(max_length=12, choices=EXPENSES_TYPE,
#                                     default='Compra')
#     item = models.CharField(max_length=100, default='')
#     description = models.TextField(blank=True)
#     unit = models.CharField(max_length=14, choices=UNIT_TYPE, default='')
#     quantity = models.IntegerField(default=0)
#     price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
#     date = models.DateField(null=True, blank=True)
#
#     @property
#     def total(self):
#         return self.quantity * self.price
#
#     def __str__(self):
#         return str(self.service_type)
#
#     class Meta:
#         ordering = ['service_type']
#         verbose_name = 'Despesa'
#         verbose_name_plural = 'Despesas'
