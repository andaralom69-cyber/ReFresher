# for j in input():
#     if j in '0123456789':
#         print('Цифра')
#         break
# else:
#     print('Nety')

# zv = 0
# pl = 0
# for i in input():
#     if i == '*':
#         zv += 1
#     if i == '+':
#         pl += 1
# print('Zvezd = ', zv)
# print('Plusov = ', pl)

# i = input()
# if i[::1] == i[::-1]:
#     print('yes')
# else:
#     print('no')

# x = input()
# print(len(x))
# print(3 * x)
# print(x[0])
# print(x[0:3])
# print(x[-3:])
# print(x[::-1])
# print(x[1:-1])

# x = input()
# if 5 <= len(x) <= 100:
#         print(x[2])
#         print(x[-2])
#         print(x[:5])
#         print(x[:-2])
#         for i in range(len(x)):
#             if i % 2 == 0 or i == 0:
#                 print(x[i])
#             else:
#                 print(x[i])
#         print(x[::-1])
#         print(x[::-2])
#         print(len(x))

# x = int(input())
# y = input()
# if len(y) <= x:
#     f = len(y)
#     h = x // f
#     if h > 0:
#         print(y * h, end='')
#         j = x - h * f
#         if  j > 0:
#             print('!' * j)
#     else:
#         print(y)

# x = input()
# if len(x) < 20:
#     if x == 'кошка':
#         print('v')
#     elif len(x) % 2 != 0:
#         print('G')
#     else:
#         print('R')
# else:
#     print('Net')

# s = input()
# print(s.capitalize())
# print(s.swapcase())
# print(s.title())
# print(s.lower())
# print(s.upper())

# s = input()
# if s == s.title():
#     print('UES')
# else:
#     print('no')

# s = input()
# if 'хорош' in s.lower():
#     print('yes')
# else:
#     print('no')

# s = input()
# print(s.swapcase())

# s = input()
# print(s.count(input()))
# print(s.startswith(input()))
# print(s.endswith(input()))
# print(s.find(input()))
# print(s.rfind(input()))
# print(s.strip())
# print(s.rstrip())
# print(s.lstrip())
# print(s.replace(input(), input()))

# s = input()
# h = 0
# for i in range(1, 10):
#     i = str(i)
#     h += s.count(i)
# print(h)

# s = input()
# if s.endswith('.com') or s.endswith('.ru') == True:
#     print('yes')
# else:
#     print('no')

# s = input()
# if s.count('f') == 1:
#     print(s.find('f'))
# elif s.count('f') > 1:
#     print(s.find('f'))
#     print(s.rfind('f'))
# else:
#     print('no')
#
# s = input()
# print(s[s.find('h')+1:s.rfind('h')])