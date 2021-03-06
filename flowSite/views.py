from django.shortcuts import render
from django.views.generic import TemplateView
import pandas as pd


class IndexView(TemplateView):
    template_name = 'index.html'


class ContactView(TemplateView):
    template_name = 'contact.html'


class BlogView(TemplateView):
    template_name = 'blog.html'


index = IndexView.as_view()
contact = ContactView.as_view()
blog = BlogView.as_view()