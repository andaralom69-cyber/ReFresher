# x = int(input())
# g = 1
# for i in range(1, x+1):
#     for j in range(i):
#         print(g, end= ' ')
#         g += 1
#     print()


# x = int(input())
# for i in range(1, x + 1):
#     for j in range(1, i + 1):
#         print(j, end="")
#     for k in range(i - 1, 0, -1):
#         print(k, end="")
#     print()


# x = int(input())
# y = int(input())
# for i in range(y):
#     for g in range(x):
#         print('*' * 1, end = ' ')
#     print()

# x = int(input())
# for i in range(1, x + 1):
#     g = 0
#     for j in range(1, i+1):
#         if i % j == 0:
#             g += 1
#     print(i, end='')
#     for h in range(g):
#         print('+', end='')
#     print()

# x = int(input())
# y = int(input())
# h = -1
# f = -1
# if x < y:
#     for i in range(x, y+1):
#         g = 0
#         for j in range(1, i+1):
#             if i % j == 0:
#                 g += j
#         if g >= f:
#             f = g
#             h = i
#     print(h, f)
#
# else:
#     print('err')

# x = int(input())
# y = 0
# for i in range(1, x + 1):
#     f = 1
#     for k in range(1, i + 1):
#         f *= k
#     y += f
#
# print(y)
#
# x = int(input())
# y = 0
# f = 1
# for i in range(1, x + 1):
#     f *= i
#     y += f
# print(y)
#
# x = int(input())
# y = int(input())
# for i in range(x, y+1):
#     g = 0
#     for j in range(1, i+1):
#         if i % j == 0:
#             g += 1
#     if  g == 2:
#         print(i)
