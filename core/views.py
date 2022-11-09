from django.shortcuts import render
from django.utils import timezone
from django.contrib import messages
from django.views.generic import TemplateView

# Create your views here.

class HomeView(TemplateView):
    template_name = "index.html"

class AboutView(TemplateView):
    template_name = "about.html"


class ServicesView(TemplateView):
    template_name = "services.html"


class ResourcesView(TemplateView):
    template_name = "resources.html"


class FinderView(TemplateView):
    template_name = "finder.html"


class ContactView(TemplateView):
    template_name = "contact.html"