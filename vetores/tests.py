from num2words import num2words

# numero = input('Digite um número: ')
#
# num_ptbr = num2words(numero, lang='en')
# print(f'Número: {num_ptbr}')
#
# print(type(numero))


list1 = ['0', '20', '16', '10', '20']
list2 = []

for i in range(0, len(list1)):
    list2.append(num2words(list1[i], lang='en'))

print(list2)


