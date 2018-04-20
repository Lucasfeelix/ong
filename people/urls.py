from django.urls import path
from . import views as v


app_name = 'people'
urlpatterns = [
    path('alunos/', v.students_list, name='students_list'),
    path('cadastrar/alunos/', v.students_create, name='students_create'),
    path('editar/aluno/<int:id>/', v.students_update, name='students_update'),
    #
    # path('doadores',),
    # path('doadores/cadastrar/', ),
    # path('doadores/editar/', ),
    #
    # path('funcionarios',),
    # path('funcionarios/cadastrar/', ),
    # path('funcionarios/editar/', ),
]