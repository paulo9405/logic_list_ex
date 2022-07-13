from django.shortcuts import render, redirect
from random import random, randrange


def home(request):
    return render(request, 'home.html')

def ex1(request):
    y = randrange(11)
    x = randrange(11)
    s = x + y
    return render(request, 'ex1.html', {'x': x, 'y': y, 's': s})