from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

# Create your views here.

def first(request):
    return HttpResponse("<h1>Hello World</h1>")

def second(request):
    return HttpResponse("<input type='text' required><br><button>Submit</button>")

def testview(request):
    name="ajith"
    names=["binoy"]
    students=[
        {"name":"Ajith","age":20},
        {"name":"Sujith","age":20},
        {"name":"Vijith","age":23},
    ]
    return render(request,"test.html",{"data":name,"list_name":names,"stu":students})


def log(request):
    if request.method=="GET":
        return render(request,"login.html")
    elif request.method=="POST":
        un=request.POST.get("user")
        ps=request.POST.get("pswd")
        return HttpResponse("Username:"+un+",password:"+ps)
    
def add(request):
    if request.method=="GET":
        return render(request,"add.html")
    elif request.method=="POST":
        f=request.POST.get("first")
        s=request.POST.get("second")
        res=int(f)+int(s)
        return HttpResponse("Result:"+str(res))


#class based views
class AddView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"add.html")
    def post(self,request,*args,**kwargs):
        f=request.POST.get("first")
        s=request.POST.get("second")
        res=int(f)+int(s)
        return HttpResponse("Result:"+str(res))

class WordView(View):
    def get(self,request):
        return render(request,"word.html")
    def post(self,request):
        w=request.POST.get("wrd")
        res=w.split()
        b={}
        for i in res:
            if i in b:
                b[i]+=1
            else:
                b[i]=1
        print(b)
        return render(request,"word.html",{"data":b})

class HomeView(View):
    def get(self,request):
        return render(request,"home.html")

