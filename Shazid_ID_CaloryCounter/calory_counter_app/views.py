from django.shortcuts import render,redirect
from .forms import UserForm,SignInForm
from django.contrib.auth import authenticate
# Create your views here.
def signup(request):
    if request.method=="POST":
        form=UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(signup)
    else:
        form=UserForm()
    return render(request,"signup.html",{'form':form})

def signin(request):
    if request.method=="POST":
        form=SignInForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            if user:
                print("user exist")
            else:
                print("user not exist")
            return redirect(signin)    
    else:                
        form=SignInForm()
        return render(request,'signin.html',{'form':form})