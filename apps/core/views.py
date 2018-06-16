from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class DashboardTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'


dashboard = DashboardTemplateView.as_view()
