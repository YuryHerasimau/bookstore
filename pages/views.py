from django.shortcuts import render
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

def error_404_view(request, exception):
    return render(request, 'error_404.html', status=404)