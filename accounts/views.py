from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import UserAdminCreationForm
from .models import User


class RegisterView(LoginRequiredMixin, CreateView):
    model = User
    template_name = 'register.html'
    form_class = UserAdminCreationForm
    success_url = reverse_lazy('core:dashboard')


register = RegisterView.as_view()
