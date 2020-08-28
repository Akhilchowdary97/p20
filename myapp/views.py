from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.core.files.storage import FileSystemStorage
from myapp.utilities import store_Image
from myapp import utilities
def trail(request):
    return HttpResponse("<h1>Project is on Air</h1>")
def base(request):
    return render(request,"base.html")
def home(request):
    return render(request,"myapp/home.html")
def profile(request):
    name="Akhil"
    return render(request,"myapp/profile.html",{'name':name})
def get_demo(request):
    name=request.GET.get('name')
    return render(request,"get_demo.html",{'name':name})
def post_demo(request):
    if request.method=="POST": 
        name=request.POST.get('name')
        return HttpResponse("<h1>Thanks for submission MR./MS. {}</h1>".format(name))
    return render(request,"post_demo.html")
def register(request):
    if request.method=="POST":
        First_Name=request.POST.get("First_Name")
        Last_Name=request.POST.get("Last_Name")
        Email=request.POST.get("Email")
        Phone_Number=request.POST.get("Phone_Number")
        Password=request.POST.get("Password")
        date=request.POST.get("birthday_day")
        month=request.POST.get("birthday_month")
        year=request.POST.get("birthday_year")
        gender=request.POST.get("sex")
        if gender=="1":
            gender="FeMale"
        else:
            gender="Male"

        send_mail("Thanks For Registration","hello Mr./Ms.{} {}\n Thanks for Registering".format(First_Name,Last_Name),
        "m.akhilchowdary97@gmail.com",[Email,],fail_silently=True)
        return redirect("home")
    return render(request,"myapp/registration.html")
def multi(request):
    if request.method=="POST":
        foods=request.POST.getlist("food")
        languages=request.POST.getlist("language")
        return HttpResponse("<h1>{}{}<h1>".format(foods,languages))
    return render(request,"multiselect.html")
def img_upld(request):
    return render(request,"img_upld.html")
def img_display(request):
    file_url=False
    if request.method=="POST" and request.FILES:
        Image1=request.FILES.get('Akh')
        Image2=request.FILES.get('Akhi')
        Image3=request.FILES.get('Akhil')
        file_urls=map(store_Image,[Image1,Image2,Image3])
    return render(request,"img_display.html",context={'file_urls':file_urls})

from myapp import forms
def builtin(request):
    if request.method=="POST":
        form=forms.SampleForm(request.POST,request.FILES)
        if form.is_valid()==False:
            return render(request,"builtin.html",{'form':form})
        else:
            data=form.cleaned_data
            Profile_Pic=data['Profile_Pic']
            utilities.store_Image(Profile_Pic)
            print(form.cleaned_data)
    form=forms.SampleForm()
    return render(request,"builtin.html",{'form':form})