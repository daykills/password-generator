from django.shortcuts import render
from django.http import HttpResponse
import random
import string

def home(request):
    return render(request, 'generator/home.html')

def password(request):
    password = ''

    length_password= int(request.GET.get('length'))
    str_characters = "!@#$%^&*" + string.ascii_lowercase + string.digits
    password = ''.join(random.choice(str_characters) for _ in range(length_password))
    return render(request, 'generator/password.html', {'password': password})

def about(request):
    return render(request, 'generator/about.html')
