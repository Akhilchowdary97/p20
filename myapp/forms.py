from django import forms
from django.core import validators
from django.core.exceptions import ValidationError
import re

def validate_name(Name):
    m=re.match('[a-zA-Z]+',Name)
    if m.group()!=Name:
        raise ValidationError("Name is Not valid")
    return Name

class SampleForm(forms.Form):
    Name=forms.CharField(max_length=200,required=True,label="Name :",
    validators=[validate_name])
    
    Email=forms.EmailField(max_length=100,required=True,label="Email :",
    validators=[validators.MinLengthValidator(10)])

    ConfirmEmail=forms.EmailField(max_length=100,required=True,label="Confirm Email :")
    IPaddress=forms.CharField(max_length=100,required=True,label="IP address :",
    validators=[validators.validate_ipv4_address])
    Password=forms.CharField(max_length=200,required=True,label="Password :",widget=forms.PasswordInput(attrs={'placeholder':"Password"}))
    Profile_Pic=forms.ImageField(max_length=200,required=False,label="Profile Pic :")
    botcacher=forms.CharField(max_length=10,required=False,widget=forms.HiddenInput)
    def clean(self,*args,**kwargs):
        cleaned_data=super().clean()
        email=cleaned_data.get("Email")
        cemail=cleaned_data.get("ConfirmEmail")
        if email==cemail:
            return cleaned_data
        self.add_error('ConfirmEmail',"Both the emails are not same")
    def clean_name(self):
	    Name=self.cleaned_data.get("Name")
	    for i in Name:
		    if not('a'<=i<='z' or 'A'<=i<='Z'):
			    raise ValidationError("Name must contain only alphabets")
	    return Name    
    def clean_botcacher(self):
        data=self.cleaned_data.get("botcacher")
        if len(data)==0:
            return data
        self.add_error("Name","Hey CHITTI I Got You")
