from django.db.models.query_utils import Q
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView

from backend.models import CustomUser
# from .forms import


class HomePageView(TemplateView):
    template_name = 'pages/home.html'


class AboutPageView(TemplateView):
    template_name = 'pages/about.html'
