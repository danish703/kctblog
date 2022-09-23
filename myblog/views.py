from django.shortcuts import render

def blog(request):
    return render(request,'blog.html')

def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')

def home(request):
    return render(request,'index.html')


def register(request):
    return render(request,'register.html')

def signin(request):
    return render(request,'login.html')