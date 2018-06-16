from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import Courses


class CoursesForm(forms.ModelForm):
    class Meta:
        model = Courses
        fields = ['name', 'price', 'students_number', 'duration']
        labels = {
            'name': _('Nome'),
            'price': _('Valor'),
            'students_number': _('Qtd. Alunos'),
            'duration': _('Duração'),
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
            'students_number': forms.TextInput(attrs={'class': 'form-control'}),
            'duration': forms.TextInput(attrs={'class': 'form-control'}),
        }