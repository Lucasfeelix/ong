from django.urls import path
from .views import alunos


app_name = 'people'
urlpatterns = [
    path('alunos', alunos, name='alunos'),
    # path('alunos/cadastrar/', ),
    # path('aluno/editar/', ),
    #
    # path('doadores',),
    # path('doadores/cadastrar/', ),
    # path('doadores/editar/', ),
    #
    # path('funcionarios',),
    # path('funcionarios/cadastrar/', ),
    # path('funcionarios/editar/', ),
]