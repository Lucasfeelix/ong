from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Courses
from .forms import CoursesForm


class CoursesCreateView(LoginRequiredMixin, CreateView):
    form_class = CoursesForm
    model = Courses
    template_name = 'cadastrar.html'
    success_url = reverse_lazy('adm:courses_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['back_url'] = reverse_lazy('adm:courses_list')
        context['type'] = 'courses'
        context['complete_title'] = 'Cadastrar curso'
        return context

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class CoursesListView(LoginRequiredMixin, ListView):
    context_object_name = 'courses'
    model = Courses
    template_name = 'listagem.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['add_url'] = reverse_lazy('adm:courses_create')
        context['complete_title'] = 'Cursos cadastrados'
        context['type'] = 'courses'
        return context


class CoursesUpdateView(LoginRequiredMixin, UpdateView):
    model = Courses
    form_class = CoursesForm
    success_url = reverse_lazy('adm:courses_list')
    template_name = 'cadastrar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['back_url'] = reverse_lazy('adm:courses_list')
        context['complete_title'] = 'Editar curso'
        context['type'] = 'courses'
        return context


courses_create = CoursesCreateView.as_view()
courses_list = CoursesListView.as_view()
courses_update = CoursesUpdateView.as_view()
