from django.urls import path
from .views import *


app_name = 'adm'
urlpatterns = [
    path('cursos/', courses_list, name='courses_list'),
    path('cursos/cadastrar/', courses_create, name='courses_create'),
    path('cursos/editar/<str:ref_adm>/<slug>/', courses_update,
         name='courses_update'),
]