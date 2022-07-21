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

def reversed_string(a_string):
    return a_string[::-1]


a = 'arara'
reversed_string(a)

if reversed_string(a) == a:
    print('E um anagrama')
else:
    print('Nao e anagrama')

