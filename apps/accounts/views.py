from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import UserAdminCreationForm
from .models import User


class RegisterView(LoginRequiredMixin, CreateView):
    model = User
    template_name = 'accounts/register.html'
    form_class = UserAdminCreationForm
    success_url = reverse_lazy('core:dashboard')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['back_url'] = reverse_lazy('core:dashboard')
        context['complete_title'] = 'Cadastrar usuário'
        return context


register = RegisterView.as_view()
