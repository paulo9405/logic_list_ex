# lst = [0] * 10
# values = [(3, 100), (5, 200), (7, 300)]
#
# for index, value in values:
#      lst[index] = value
#
# print(lst)  # [0, 0, 0, 100, 0, 200, 0, 300, 0, 0]

'''
Intermediário 7. Leia dois vetores de 20 posições e
calcule um terceiro vetor contendo, nas posições pares
os valores do primeiro e nas posições impares os valores do segundo.
'''

lista = [16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 20, 19, 18]

pares = []
impares = []
for i in range(len(lista)):
     if lista[i] % 2 == 0:
          pares.append(lista[i])
     else:
          impares.append(lista[i])

print(pares)
print(impares)