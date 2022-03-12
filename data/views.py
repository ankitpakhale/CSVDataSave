from django.http import HttpResponse
from django.shortcuts import render
from .models import *
import csv
import pandas
# Create your views here.

def index(request):    
    if request.POST:
        f = request.POST['file']
        with open(f, 'r') as f:
            a1 = f.readlines()
            a = a1[1::]
            for i in a:
                print(i[0])

    return render(request, 'index.html')
