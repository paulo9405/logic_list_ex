# a = ['1', ' 2', ' 3', ' 4', ' 9']
#
# b = []
#
# for i in a:
#     c = i.replace(' ', '')
#     b.append(c)
#
# print(b)


a = ['1', '2', '3', '4', '9', '8', '16', '15']
a_int = []

count = 0
for i in a:
    a_int.append(int(i))

for i in a_int:
    if i%2 == 0:
        count += 1

print(a_int)

print(count)
