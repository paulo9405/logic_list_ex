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

# a = [1, 2, 3]
#
# b = [20, 21, 22]
#
# # c = [None, None, None, None, None, None]
# c = [0]*6


# for i in c:
#     if c.index(i) % 2 == 0:
#         for d in a:
#             i = d

'''try ex 7'''
# for index, v in enumerate(c):
#     t = []
#     t = index
#
# #     # else:
#     #     for e in b:
#     #         c[index] = e
#
# print(t)
#
# print(c)
# # 0 2 4 | 1 3 5


a = [0, 2, 4, 6, 8]

b = [1, 3, 5, 7, 9]

c = []

va = 0
vb = 0

for i in range(0, 10):
    if i % 2 == 0:
        c.append(a[va])
        va += 1

    else:
        c.append(b[vb])
        vb += 1


print(c)




