from django.http import HttpResponseRedirect
from django.urls import path
from .views import dashboard

app_name = 'core'
urlpatterns = [
    path('', lambda x: HttpResponseRedirect('dashboard/')),
    path('dashboard/', dashboard, name='dashboard'),
]
