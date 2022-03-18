from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

def index(request):    
    msg = ''
    if request.POST:
# -----------------------Code 1----------------------------------------------------
        # f = request.POST['file']
        # print(f)
        # with open(f, 'r') as f:
        #     a1 = f.readlines()
        #     a = a1[1::]
        #     for i in a:
        #         l = i.split(',')                
        #         q = Entry.objects.filter(pname = l[0])
        #         try:
        #             if not q:
        #                 e = Entry()
        #                 e.pname = l[0]
        #                 e.pqty = l[1]
        #                 e.pprice = l[2]
        #                 e.save()
        #                 msg = "Product Saved Properly"
        #                 print(msg)    
        #             msg = "Product Already Exists"
        #             print(msg)
        #         except:
        #             return HttpResponse("Please Enter Proper Data")

# -----------------------Code 2----------------------------------------------------
        f = request.FILES.get('file').read()
        print(f)
        f=str(f).split('\\n')
        
        # f=f.split(',')
        # count=0
        
        for i in f[1:len(f)-1]:
            i=i.split(',')
            q = Entry.objects.filter(pname=i[0])
            try:
                if not q :
                    e = Entry()
                    e.pname = i[0]
                    e.pqty = i[1]
                    e.pprice = i[2].replace("\\r","")
                    e.save()
                    msg = "Product Saved Properly"
                    print(msg)
                else:
                    msg = "Product Already Exists"
                    print(msg)
            except:
                return HttpResponse('enter proper data')
    return render(request, 'index.html', {'msg': msg})
