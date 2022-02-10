from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
# from .models import Homepage

def home(request):

    return render( request,'pages/home.html')


class about(TemplateView):
    template_name = 'pages/about.html' 

class contact(TemplateView):
    template_name = 'pages/contact.html' 

class blog(TemplateView):
    template_name = 'blogs/blogs.html' 