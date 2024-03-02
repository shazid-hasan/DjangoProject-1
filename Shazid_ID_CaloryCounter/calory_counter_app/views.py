from django.shortcuts import render
from .forms import UserForm

# Create your views here.
def signup(request):
    form=UserForm()
    return render(request,"signup.html",{'form':form})