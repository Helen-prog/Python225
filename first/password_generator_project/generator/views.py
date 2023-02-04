from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    lst = list(range(6, 15))
    return render(request, 'generator/home.html', {'lst': lst})


def password(request):
    char = [chr(i) for i in range(97, 123)]

    length = int(request.GET.get('length'))
    psw = ''
    for i in range(length):
        psw += random.choice(char)
    return render(request, 'generator/password.html', {'password': psw})
