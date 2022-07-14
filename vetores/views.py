from django.shortcuts import render, redirect
from random import random, randrange


def home(request):
    return render(request, 'home.html')

# def ex1(request):
#     y = randrange(11)
#     x = randrange(11)
#     s = x + y
#     return render(request, 'ex1.html', {'x': x, 'y': y, 's': s})

# def ex1(request):
#     x = None
#     y = None
#     s = None
#     data = None
#     if request.method == "POST":
#         data = int(request.POST.get('valueuser'))
#
#         if data.count() > 3:
#
#             y = randrange(data)
#             x = randrange(data)
#             s = x + y
#     return render(request, 'ex1.html', {'x': x, 'y': y, 's': s, 'data':data})


def ex1(request):
    list_value = None
    x = None
    y = None
    x_p = None
    y_p = None
    sum = None

    if request.method == "POST":
        value_1 = int(request.POST.get('value_1'))
        value_2 = int(request.POST.get('value_2'))
        value_3 = int(request.POST.get('value_3'))
        value_4 = int(request.POST.get('value_4'))
        x = int(request.POST.get('value_x'))
        y = int(request.POST.get('value_y'))
        list_value = [value_1, value_2, value_3, value_4]
        x_p = list_value[x]
        y_p = list_value[y]
        sum = list_value[x] + list_value[y]
    return render(request, 'ex1.html', {'list_value': list_value,
                                        'x': x, 'y': y, 'x_p': x_p,
                                        'y_p': y_p, 'sum': sum})