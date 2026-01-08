# def b(h, w):
#     for i in range(h):
#         print(' 67 ' * w)
# b(6, 7)

# def convert_to_celsius(temp):
#     result = (5 / 9) * (temp - 32)
#     return result
#
# temp = float(input('Bвeдитe количество градусов по Фаренгейту: '))
# celsius = convert_to_celsius(temp)
# print(celsius)

# def g(a, b):
#     c = (a**2 + b**2) ** 0.5
#     return c
#
# print(g(3,4))
# print(g(5,12))
# print(g(1,1))

# def dist(x1, x2, y1, y2):
#     d = ((x1 - x2)**2 + (y1-y2)**2) ** 0.5
#     return d
# x1, x2 = float(input()), float(input())
# y1, y2 = float(input()), float(input())
# print(dist(x1, x2, y1, y2))

# def sum(n):
#     result = 0
#     while n > 0:
#         result += n % 10
#         n //= 10
#     return result
#
# n = int(input())
# print(sum(n))

# def s(n):
#     return sum(n) / len(n)
# n = list(range(1, 1000, 46))
# print(s(n))

# def s(n):
#     result = 1
#     for i in n:
#         result *= i
#     return result
# print(s([4,4,4,4]))

# def s(y,m,day):
#     return f'{y}-{m}-{day}'
#     return f'{y} - {m} - {day}'
# print(s(31,10,2025))

# def g_h (n, h):
#     m_h = max(h)
#     i_m_h = h.index(m_h)
#     return n [i_m_h]
# print(g_h(['Андрей', 'Валерия', 'Елена', 'Николай', 'Жанна'], [ 1.75, 1.61, 1.65, 1.83, 1.64]))

# def r(w, h):
#     print('*' * w)
#     for i in range(h):
#         print('*' + ' ' * (w-2) + '*')
#     print('*' * w)
# r(10,14)

# def x(y):
#     for j in range(y+1):
#             print('*' * j)
# x(8)

# def miles(km):
#     return km * 0.6214
# km = float(input())
# print(miles(km))

# def ok(x):
#     if x % 1 >= 0.5:
#         x += 1
#         x = int(x)
#         print(x)
#     else:
#         x = int(x)
#         print(x)
# x = float(input())
# ok(x)

