from django.shortcuts import render,redirect
from django.views.generic import View
from django.http import HttpResponse
from .forms import DoctorForm,PatForm
from django.contrib import messages

# Create your views here.

class AddDocView(View):
    def get(self,request):
        form=DoctorForm()
        return render(request,"adddoc.html",{"form":form})
    def post(self,request):
        form_data=DoctorForm(data=request.POST)
        if form_data.is_valid():
            print(form_data.cleaned_data.get("name"))
            print(form_data.cleaned_data.get("age"))
            print(form_data.cleaned_data.get("email"))
            print(form_data.cleaned_data.get("qualification"))
            print(form_data.cleaned_data.get("adhaar"))
        # print(name,age,qlf,adhaar,email)
            messages.success(request,"Doctor added Successfully")
            messages.error(request,"Details not stored")
            return redirect("h")
        return render(request,"adddoc.html",{"form":form_data})
    
class AddPateintView(View):
    def get(self,request):
        form=PatForm()
        return render(request,"addpat.html",{"form":form})
