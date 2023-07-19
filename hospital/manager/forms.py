from typing import Any, Dict
from django import forms
import re


class DoctorForm(forms.Form):
    name=forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter Name"}))
    age=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control","placeholder":"Enter Age"}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control","placeholder":"Enter Email ID"}))
    qualification=forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter Qualification"}))
    adhaar=forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Enter Adhaar Numbetr"}))

    def clean(self):
        data=super().clean()
        ag=data.get("age")
        ad=data.get("adhaar")
        if ag<0:
            msg="Enter valid Age(must be greater than 0)"
            self.add_error("age",msg)
        if len(ad)!=12:
            self.add_error("adhaar","The adhaar number should be 12 digits")
        # print(re.search("\D+",ad),ad)
        if re.search("\D+",ad):
            self.add_error("adhaar","Adhaar number should be completely numerical")
        return data


class PatForm(forms.Form):
    name=forms.CharField(max_length=100)
    age=forms.IntegerField()
    blood=forms.CharField(max_length=100)
    phone=forms.IntegerField()
    address=forms.CharField(max_length=500)