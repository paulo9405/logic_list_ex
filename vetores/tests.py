# a = ['1', ' 2', ' 3', ' 4', ' 9']
#
# b = []
#
# for i in a:
#     c = i.replace(' ', '')
#     b.append(c)
#
# print(b)

#
# a = [-2, 3, 7, -5]
t = ['-2', '3', '7', '-5']
# b = []
# c = []
# #
# s = t.replace('-2', '0')
# print(s)

# for i in a:
#     if i < 0:
#         c = i
#
#         c.append(c)

a = [-2, 3, 7, -5]

# a = [i.replace(-2, 0) for i in a ]
#
# print(a)
#
# x = '0'
# y = 1
#
# if y > x:
#     print('X e maior')

# my_list=[-5,-10,7,5,6,-8,5,15]
my_list = [-2, 3, 7, -5]
for index, value in enumerate(my_list):
    if value < 0:
      my_list[index] = 0

print(my_list)


