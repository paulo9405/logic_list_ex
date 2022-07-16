from django.shortcuts import render, redirect


def home(request):
    return render(request, 'home.html')


def ex1(request):
    list_value = None
    x = None
    y = None
    x_p = None
    y_p = None
    sum = None

    if request.method == "POST":
        value_1 = request.POST.get('value_1')
        list_value = value_1.split(",")

        x = int(request.POST.get('value_x'))
        y = int(request.POST.get('value_y'))

        x_p = list_value[x]
        y_p = list_value[y]
        sum = int(list_value[x]) + int(list_value[y])

    return render(request, 'ex1.html', {'list_value': list_value,
                                        'x': x, 'y': y, 'x_p': x_p,
                                        'y_p': y_p, 'sum': sum})


def ex2(request):
    start_vector = None
    ending_vector = None
    vet = []
    if request.method == "POST":
        start_vector = int(request.POST.get('value_x'))
        ending_vector = int(request.POST.get('value_y'))
        for i in range(start_vector, ending_vector):
            if i % 2 == 1:
                vet.append(i)
    return render(request, 'ex2.html', {'vet': vet})


def ex3(request):
    vet = []
    if request.method == 'POST':
        value_1 = request.POST.get('value_x')
        vet = value_1.split(",")
        div = int(len(vet) / 2)
        a = [vet[div:], vet[:div]]
        if len(vet) > 4 or len(vet) < 4:
            erro = 'Plase write exactly 4 values.'
            return render(request, 'ex3.html', {'erro': erro})
    return render(request, 'ex3.html', {'vet': vet, 'a': a})