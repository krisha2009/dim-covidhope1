from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request,'homepage.html')

def info(request):
    return render(request,'info.html')

def login(request):
    return render(request,'login.html')

def signup(request):
    return render(request,'signup.html')