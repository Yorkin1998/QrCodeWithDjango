from django.shortcuts import render
from .models import Students

def home(request,pk,some_kind_token):
    print(some_kind_token)
    getter=Students.objects.get(id=pk)
    return render(request,'index.html',context={'getter':getter})
