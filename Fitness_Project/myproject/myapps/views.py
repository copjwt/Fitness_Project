from django.shortcuts import render
from django.http import  HttpResponse

# Create your views here.
def signup(request):
    return render(request,"signup.html")

def signin(request):
    return render(request,"signin.html")

def main(request):
    return render(request,"main.html")