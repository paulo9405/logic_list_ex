from django.test import TestCase

from random import random, randrange
# n=1,9,3
#
# print(randrange(11))
# print(randrange(11))
'''
tabela = [ int(input("Informe um valor inteiro, faltam "+str(12-x)+"\n"))
           for x in range(12)]

tabela = [ int(random()*100-30)
           for x in range(12)]

print("Eis os doze valores" )

print( [ '{0:3d}'.format(x) for x in tabela] )

primeiro = int(input("Informe o X entre 1 e 12"))

segundo = int(input("Informe o Y também entre 1 e 12"))

print("O elemento",primeiro,"vale",tabela[primeiro-1])

print("O elemento",segundo,"vale",tabela[segundo-1])

print("A soma é",tabela[primeiro-1]+tabela[segundo-1])
'''

data = []
n = int(input('Enter how many elements you want: '))
for i in range(0, 3):
    x = input('Enter the numbers into the array: ')
    data.append(x)
print(data)