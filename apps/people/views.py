from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Donors, Employees, Students
from .forms import DonorsForm, EmployeesForm, StudentsForm


class StudentsCreateView(LoginRequiredMixin, CreateView):
    form_class = StudentsForm
    model = Students
    template_name = 'cadastrar.html'
    success_url = reverse_lazy('people:students_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['back_url'] = reverse_lazy('people:students_list')
        context['type'] = 'students'
        context['complete_title'] = 'Cadastrar aluno'
        return context

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)
    

class StudentsListView(LoginRequiredMixin, ListView):
    context_object_name = 'students'
    model = Students
    template_name = 'listagem.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['add_url'] = reverse_lazy('people:students_create')
        context['complete_title'] = 'Alunos cadastrados'
        context['type'] = 'students'
        return context


class StudentsUpdateView(LoginRequiredMixin, UpdateView):
    model = Students
    form_class = StudentsForm
    success_url = reverse_lazy('people:students_list')
    template_name = 'cadastrar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['back_url'] = reverse_lazy('people:students_list')
        context['complete_title'] = 'Editar aluno'
        context['type'] = 'students'
        return context


class DonorsCreateView(LoginRequiredMixin, CreateView):
    model = Donors
    form_class = DonorsForm
    template_name = 'cadastrar.html'
    success_url = reverse_lazy('people:donors_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['back_url'] = reverse_lazy('people:donors_list')
        context['complete_title'] = 'Cadastrar doador'
        context['type'] = 'donors'
        return context

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class DonorsListView(LoginRequiredMixin, ListView):
    context_object_name = 'donors'
    model = Donors
    template_name = 'listagem.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['add_url'] = reverse_lazy('people:donors_create')
        context['complete_title'] = 'Doadores cadastrados'
        context['type'] = 'donors'
        return context


class DonorsUpdate(LoginRequiredMixin, UpdateView):
    model = Donors
    form_class = DonorsForm
    success_url = reverse_lazy('people:donors_list')
    template_name = 'cadastrar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['back_url'] = reverse_lazy('people:donors_list')
        context['complete_title'] = 'Editar doador'
        context['type'] = 'donors'
        return context


class EmployeesCreateView(LoginRequiredMixin, CreateView):
    model = Employees
    form_class = EmployeesForm
    template_name = 'cadastrar.html'
    success_url = reverse_lazy('people:employees_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['back_url'] = reverse_lazy('people:employees_list')
        context['complete_title'] = 'Cadastrar funcionário'
        context['type'] = 'employees'
        return context

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class EmployeesListView(LoginRequiredMixin, ListView):
    context_object_name = 'employees'
    model = Employees
    template_name = 'listagem.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['add_url'] = reverse_lazy('people:employees_create')
        context['complete_title'] = 'Funcionários cadastrados'
        context['type'] = 'employees'
        return context


class EmployeesUpdate(LoginRequiredMixin, UpdateView):
    model = Employees
    form_class = EmployeesForm
    success_url = reverse_lazy('people:employees_list')
    template_name = 'cadastrar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['back_url'] = reverse_lazy('people:employees_list')
        context['complete_title'] = 'Editar funcionário'
        context['type'] = 'employees'
        return context


students_create = StudentsCreateView.as_view()
students_list = StudentsListView.as_view()
students_update = StudentsUpdateView.as_view()

donors_create = DonorsCreateView.as_view()
donors_list = DonorsListView.as_view()
donors_update = DonorsUpdate.as_view()

employees_create = EmployeesCreateView.as_view()
employees_list = EmployeesListView.as_view()
employees_update = EmployeesUpdate.as_view()
