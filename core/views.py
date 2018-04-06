from django.shortcuts import render
from django.views.generic import TemplateView


def index(request):
    return render(request, 'index.html')


class ListTemplateView(TemplateView):
    template_name = 'list_data.html'


list_template_view = ListTemplateView.as_view()
