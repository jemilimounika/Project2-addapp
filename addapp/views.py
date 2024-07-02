from django.shortcuts import render
from django.http import HttpResponse
def input(request):

    return render(request,'input.html')
def add(request):
    x=request.GET["t1"]
    y=request.GET["t2"]
    i=int(x)
    j=int(y)
    z=i+j
    res=HttpResponse("the SUM is"+str(z))
    return res

# Create your views here.
