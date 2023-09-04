from django.shortcuts import render
from .models import Myself
from apps.project.models import Project

# Create your views here.


def index(request):
    myself = Myself.objects.first()
    projects = Project.objects.all()
    ctx = {"myself": myself, "projects": projects}
    return render(request, "index.html", ctx)
