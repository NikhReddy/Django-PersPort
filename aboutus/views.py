from django.shortcuts import render
from .models import Project

# Create your views here.
def aboutus(request):
    project = Project.objects.all()
    return render(request,'aboutus/ab.html',{'project':project})