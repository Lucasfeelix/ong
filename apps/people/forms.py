from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import Donors, Employees, Students


class StudentsForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = ['address', 'cellphone', 'cep', 'city', 'civil_status',
                  'comments', 'country', 'cpf', 'date_of_birth', 'email',
                  'fathers_name', 'gender', 'home_phone', 'last_name',
                  'mothers_name', 'name', 'neighborhood', 'number',
                  'occupation', 'rg', 'scholarity', 'school', 'time', 'uf']
        labels = {
            'address': _('Endereço'),
            'cellphone': _('Celular'),
            'cep': _('CEP'),
            'city': _('Cidade'),
            'civil_status': _('Estado civil'),
            'comments': _('Informações Adicionais'),
            'country': _('País'),
            'cpf': _('CPF'),
            'date_of_birth': _('Data de aniversário'),
            'email': _('E-mail'),
            'fathers_name': _('Nome do pai'),
            'gender': _('Gênero'),
            'home_phone': _('Telefone de casa'),
            'last_name': _('Sobrenome'),
            'mothers_name': _('Nome da mãe'),
            'name': _('Nome'),
            'neighborhood': _('Bairro'),
            'number': _('Número'),
            'occupation': _('Profissão'),
            'rg': _('RG'),
            'scholarity': _('Escolaridade'),
            'school': _('Instituição'),
            'time': _('Período'),
            'uf': _('UF'),
        }
        widgets = {
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'cellphone': forms.TextInput(
                attrs={'class': 'form-control mobile-phone-number'}),
            'cep': forms.TextInput(attrs={'class': 'form-control cep'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'civil_status': forms.Select(attrs={'class': 'form-control'}),
            'comments': forms.Textarea(attrs={'class': 'form-control',
                                              'rows': '2'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control cpf'}),
            'date_of_birth': forms.DateInput(
                attrs={'class': 'form-control date'}),
            'email': forms.TextInput(attrs={'class': 'form-control email'}),
            'fathers_name': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'home_phone': forms.TextInput(
                attrs={'class': 'form-control phone-number'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'mothers_name': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'neighborhood': forms.TextInput(attrs={'class': 'form-control'}),
            'number': forms.TextInput(attrs={'class': 'form-control'}),
            'occupation': forms.TextInput(attrs={'class': 'form-control'}),
            'rg': forms.TextInput(attrs={'class': 'form-control rg'}),
            'scholarity': forms.Select(attrs={'class': 'form-control'}),
            'school': forms.TextInput(attrs={'class': 'form-control'}),
            'time': forms.Select(attrs={'class': 'form-control'}),
            'uf': forms.Select(attrs={'class': 'form-control'}),
        }


class DonorsForm(forms.ModelForm):
    class Meta:
        model = Donors
        fields = ['address', 'cellphone', 'cep', 'city', 'civil_status',
                  'comments', 'country', 'cpf', 'date_of_birth', 'email',
                  'fathers_name', 'gender', 'home_phone', 'last_name',
                  'mothers_name', 'name', 'neighborhood', 'number',
                  'occupation', 'rg', 'uf']
        labels = {
            'address': _('Endereço'),
            'cellphone': _('Celular'),
            'cep': _('CEP'),
            'city': _('Cidade'),
            'civil_status': _('Estado civil'),
            'comments': _('Informações Adicionais'),
            'country': _('País'),
            'cpf': _('CPF'),
            'date_of_birth': _('Data de aniversário'),
            'email': _('E-mail'),
            'fathers_name': _('Nome do pai'),
            'gender': _('Gênero'),
            'home_phone': _('Telefone de casa'),
            'last_name': _('Sobrenome'),
            'mothers_name': _('Nome da mãe'),
            'name': _('Nome'),
            'neighborhood': _('Bairro'),
            'number': _('Número'),
            'occupation': _('Profissão'),
            'rg': _('RG'),
            'uf': _('UF'),
        }
        widgets = {
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'cellphone': forms.TextInput(
                attrs={'class': 'form-control mobile-phone-number'}),
            'cep': forms.TextInput(attrs={'class': 'form-control cep'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'civil_status': forms.Select(attrs={'class': 'form-control'}),
            'comments': forms.Textarea(attrs={'class': 'form-control',
                                              'rows': '2'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control cpf'}),
            'date_of_birth': forms.DateInput(
                attrs={'class': 'form-control date'}),
            'email': forms.TextInput(attrs={'class': 'form-control email'}),
            'fathers_name': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'home_phone': forms.TextInput(
                attrs={'class': 'form-control phone-number'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'mothers_name': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'neighborhood': forms.TextInput(attrs={'class': 'form-control'}),
            'number': forms.TextInput(attrs={'class': 'form-control'}),
            'occupation': forms.TextInput(attrs={'class': 'form-control'}),
            'rg': forms.TextInput(attrs={'class': 'form-control rg'}),
            'uf': forms.Select(attrs={'class': 'form-control'}),
        }


class EmployeesForm(forms.ModelForm):
    class Meta:
        model = Employees
        fields = ['address', 'cellphone', 'cep', 'city', 'civil_status',
                  'comments', 'country', 'cpf', 'date_of_birth', 'email',
                  'fathers_name', 'gender', 'home_phone', 'last_name',
                  'mothers_name', 'name', 'neighborhood', 'number',
                  'occupation', 'rg', 'uf', 'baghelped', 'salary',
                  'employeestype']
        labels = {
            'address': _('Endereço'),
            'cellphone': _('Celular'),
            'cep': _('CEP'),
            'city': _('Cidade'),
            'civil_status': _('Estado civil'),
            'comments': _('Informações Adicionais'),
            'country': _('País'),
            'cpf': _('CPF'),
            'date_of_birth': _('Data de aniversário'),
            'email': _('E-mail'),
            'fathers_name': _('Nome do pai'),
            'gender': _('Gênero'),
            'home_phone': _('Telefone de casa'),
            'last_name': _('Sobrenome'),
            'mothers_name': _('Nome da mãe'),
            'name': _('Nome'),
            'neighborhood': _('Bairro'),
            'number': _('Número'),
            'occupation': _('Profissão'),
            'rg': _('RG'),
            'uf': _('UF'),
            'baghelped': _('Bolsa Auxílio'),
            'salary': _('Valor bolsa auxílio'),
            'employeestype': _('Tipo de serviço'),
        }
        widgets = {
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'cellphone': forms.TextInput(
                attrs={'class': 'form-control mobile-phone-number'}),
            'cep': forms.TextInput(attrs={'class': 'form-control cep'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'civil_status': forms.Select(attrs={'class': 'form-control'}),
            'comments': forms.Textarea(attrs={'class': 'form-control',
                                              'rows': '2'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control cpf'}),
            'date_of_birth': forms.DateInput(
                attrs={'class': 'form-control date'}),
            'email': forms.TextInput(attrs={'class': 'form-control email'}),
            'fathers_name': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'home_phone': forms.TextInput(
                attrs={'class': 'form-control phone-number'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'mothers_name': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'neighborhood': forms.TextInput(attrs={'class': 'form-control'}),
            'number': forms.TextInput(attrs={'class': 'form-control'}),
            'occupation': forms.TextInput(attrs={'class': 'form-control'}),
            'rg': forms.TextInput(attrs={'class': 'form-control rg'}),
            'uf': forms.Select(attrs={'class': 'form-control'}),
            'employeestype': forms.Select(attrs={'class': 'form-control'}),
            'salary': forms.TextInput(
                attrs={'class': 'form-control money-real'}),
            'baghelped': forms.Select(attrs={'class': 'form-control'}),
        }