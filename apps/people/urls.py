from django.urls import path
from .views import *


app_name = 'people'
urlpatterns = [
    path('alunos/', students_list, name='students_list'),
    path('alunos/cadastrar/', students_create, name='students_create'),
    path('aluno/editar/<str:ref_person>/<slug>/', students_update,
         name='students_update'),

    path('doadores/', donors_list, name='donors_list'),
    path('doadores/cadastrar/', donors_create, name='donors_create'),
    path('doadores/editar/<str:ref_person>/<slug>', donors_update,
         name='donors_update'),

    path('funcionarios', employees_list, name='employees_list'),
    path('funcionarios/cadastrar/', employees_create, name='employees_create'),
    path('funcionarios/editar/<str:ref_person>/<slug>', employees_update,
         name='employees_update'),
]
