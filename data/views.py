from django.http import HttpResponse
from django.shortcuts import render
from .models import *
import csv
# Create your views here.

def index(request):
    f = request.POST['file']
    print(f)
    
    return render(request, 'index.html')

# def CSV(request):
#     # data_frame = pandas.read_csv('app1/Static/Data.csv')
#     with open('app1/Static/Data.csv') as csvfile:
#         reader = csv.DictReader(csvfile)
#         for row in reader:
#             p = Entry(name=row['Name'], address=row['Address'],email=row['Email'],m_no = row['M_No'])
#             p.save()
#     return HttpResponse("Hello World")