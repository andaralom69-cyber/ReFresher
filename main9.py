# i = ""
# g = -1
# while i != "end" and i != "stop" and i != 'enough':
#     i = input()
#     g += 1
# print(g)

# i = ""
# x = ''
# while i != "END":
#     x += '\n' + i
#     i = input()
# print(x)

# i = ""
# x = ''
# while i != "END" and i != 'end':
#     x += '\n' + i
#     i = input()
# print(x)

# x = 0
# temp = 0
# while x >= 0:
#     x = int(input())
#     temp += x
# print(temp)

# monet = 0
# x = int(input())
# while x != 0:
#     if x >= 25:
#         monet += x // 25
#         x %= 25
#     elif x >= 10:
#         monet += x // 10
#         x %= 10
#     elif x >= 5:
#         monet += x // 5
#         x %= 5
#     elif x >= 1:
#         monet += x // 1
#         x %= 1
# print(monet)

# n = int(input())
# while n > 0:
#     d = n % 10
#     print(d)
#     n = n // 10

# x = int(input())
# summ = 0
# proiz = 1
# last = x % 10
# dlina = str(x)
# dlina = len(dlina)
# while x >= 10:
#     summ += x % 10
#     proiz *= x % 10
#     x = x // 10
# print('Сумма цифр равна = ', summ+x)
# print('Первая цифра = ', x)
# print('Сумма цифр первого и последнего = ', x + last)
# print('Произведение цифр = ', proiz*x)
# print('Кол-во цифр = ', dlina)
# print('Среднее ариф. = ', (summ + x) / dlina)

# x = int(input('Input your number '))
# skidka = 0
# konsum = 0
# temp = 0
# if 0 < x < 5000:
#     skidka += 5
# elif 5000 < x < 15000:
#     skidka += 12
# elif 15000 < x <= 25000:
#     skidka += 20
# elif x > 25000:
#     skidka += 30
# temp = x // 100 * skidka
# konsum += x - temp
# print('Skidka = ', temp)
# print('Konechnaya summa = ', konsum)

# x = int(input())
# c = x % 4
# z = x % 100
# v = x % 400
# if (c == 0 and z != 0) or v == 0:
#     print(x, '- Високосный')
# else:
#     print(x, '- Обычный год')

# Y = ''
# while Y != 'y' and Y != 'Y':
#     x = int(input('x: '))
#     y = int(input('y: '))
#     sum = x + y
#     print('Summa: ', sum)
#     Y = str(input("Y or y for exit: "))





