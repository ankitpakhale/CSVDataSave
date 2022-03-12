from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):    
    if request.POST:
        f = request.POST['file']
        with open(f, 'r') as f:
            a1 = f.readlines()
            a = a1[1::]
            for i in a:
                l = i.split(',')                
                q = Entry.objects.filter(pname = l[0])
                if not q:
                    e = Entry()
                    e.pname = l[0]
                    e.pqty = l[1]
                    e.pprice = l[2]
                    e.save()
                    msg = "Product Saved Properly"
                    print(msg)        
                else:
                    msg = "Product Already Exists"
                    print(msg)        

    return render(request, 'index.html', {'msg': msg})
