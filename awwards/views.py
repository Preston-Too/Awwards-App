from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import *


@login_required(login_url='/accounts/login/')
def home(request):
    projects = Projects.objects.all()
    context = {
    "projects":projects,
    }
    return render(request, 'index.html', locals())