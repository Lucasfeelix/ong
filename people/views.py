from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, ListView
from .models import Students


class StudentsCreateView(CreateView):
    model = Students


class StudentsUpdateView(UpdateView):
    model = Students


class StudentsListView(ListView):
    model = Students
    template_name = 'people/people_list.html'

    def get_context_data(self, **kwargs):
        context = super(StudentsListView, self).get_context_data(**kwargs)
        context['complete_title'] = 'Alunos'
        context['type'] = 'Students'
        return context


students_create = StudentsCreateView.as_view()
students_update = StudentsUpdateView.as_view()
students_list = StudentsListView.as_view()