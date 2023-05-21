from django.shortcuts import render,HttpResponse        

# Create your views here.
def index(request):
    c={
        "variable":"this my fiest variable"
    }
    return render(request,"index.html",c)
   # return HttpResponse("This is home page")

def about(request):
    return HttpResponse("This is about page")


def Dell(request):
    return render(request,'Dell.html')
    #return HttpResponse("This is service page")
def hp(request):
    return render(request,'hp.html')

def Lenovo(request):
    return render(request,'Lenovo.html')

