from django.shortcuts import render
from .models import Myself

# Create your views here.


def index(request):
    myself = Myself.objects.first()
    ctx = {"myself": myself}
    return render(request, "index.html", ctx)
