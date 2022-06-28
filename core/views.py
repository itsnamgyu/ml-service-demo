from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

from ml.models import CatDogClassifier


class HomeView(TemplateView):
    template_name = "core/home.html"

