
a = ['1', '2', '3', '4', '5', '6']

b = [a[3], a[4], a[5], a[0], a[1], a[2], ]

c = int(len(a)/2)

if len(a) % 2 == 1:
    print(False)

print([a[c:], a[:c]])