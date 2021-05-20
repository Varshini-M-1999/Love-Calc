from django.shortcuts import render
from pyth import cal
from .models import documents
# Create your views here.
def home(request):
    if request.method=="POST":
        fname=request.POST['fname']
        lname=request.POST['lname']
        #docs=documents(fname=fname,lname=lname)
       #docs.save()
        #print(fname)
        Result=cal()
        a=fname.lower
        b=lname.lower
        if 'tejas' in fname and 'nayana' in lname:
            Result="100% love+marriage=rugby team"
    
        Result=str(Result)+"%"
        return render(request,'result.html',{"fname":fname,"lname":lname,"Result":Result})
    else:
        #print("abcd")
        return render(request,'home.html')
