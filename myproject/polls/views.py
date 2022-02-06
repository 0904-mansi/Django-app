from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html', {'name':'Mansi'})


def add(request):
    first=int(request.GET['num1'])
    second=int(request.GET['num2'])
    res=first+second
    return render(request,'result.html', {'result':res})