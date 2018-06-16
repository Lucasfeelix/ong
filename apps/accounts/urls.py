from django.urls import path
from .views import register

app_name = 'accounts'
urlpatterns = [
    path('cadastro-usuario/', register, name='register'),
]