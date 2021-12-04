from django.shortcuts import render
from .models import Students

def home(request,pk):
    getter=Students.objects.get(id=pk)
    return render(request,'index.html',context={'getter':getter})
