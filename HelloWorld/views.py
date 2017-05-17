from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


class HomePage(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)


class Support(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'support.html', context=None)
