from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')


def detail(request):
    return render(request, 'detail.html')


def login(request):
    return render(request, 'login.html')


def regist(request):
    return render(request, 'register.html')

def verif(request):
    return render(request, 'registration_success.html')