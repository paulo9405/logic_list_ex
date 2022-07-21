# a = 'paulo'
#
# a = a.re

'''
str = "rua"

b = "rua"

a = "arara"

reversed_string=''.join(reversed(str))

print(reversed_string)

if reversed_string == b:
    print('E um anagrama')
else:
    print('Nao e anagrama')
'''




# v1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# v2 = [11, 12, 13, 14, 15, 16, 17, 18, 19]
# v3 = [21, 22, 23, 24, 25, 26, 27, 28, 29]
#
# v4 = [1, 2, 3]
# v5 = [11, 12, 13]
# v6 = [21, 22, 23]
#
#
# # s = len(a) / 3
# b = v1[:3], v2[6:], v3[6:]
#
# a = v4[:1], v5[2:], v6[2:]
#
# print('B :', b)
#
# print('A: ', a)

v1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
v2 = [11, 12, 13, 14, 15, 16, 17, 18, 19]
v3 = [21, 22, 23, 24, 25, 26, 27, 28, 29]

a = []

# for i in a:
for v11 in v1:
    a[:3] = v1[:3]

for v22 in v2:
    a[3:6] = v2[3:6]

for v33 in v3:
    a[6:] = v3[6:]

print('A: ', a)

print(len(v3))

