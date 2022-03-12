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
                l = i.split(',')
                # print(l[0], l[1], l[2])
                
                e = Entry()
                e.pname = l[0]
                e.pqty = l[1]
                e.pprice = l[2]
                e.save()
                
                
                # print(l[2][:-1])

    return render(request, 'index.html')
