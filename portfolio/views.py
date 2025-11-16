from django.shortcuts import render , HttpResponse, redirect
from . models import  Project,  Certificate
from django.contrib import messages
from django.core.mail import send_mail




import traceback

# Create your views here.
def home(request):
    projects = Project.objects.all().order_by('-date_completed')
    certificates = Certificate.objects.all()
    for project in projects:
        project.tech_list = [tech.strip() for tech in project.tech_stack.split(',')]

    context = {"projects": projects, "certificates": certificates}
    return render(request, 'portfolio/home.html', context)




