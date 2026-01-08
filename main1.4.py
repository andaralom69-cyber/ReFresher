# x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(len(x))
# if 2 in x:
#     print('2 est v x')
#
# if 0 not in x:
#     print('0 nety v x')
#
# x[2] = 4
# x[3] = 78
# print(x)

# print([1,2,3,4]+[5,6,7,8])
# print([7,8]*3)
# print([0]*10)
# print('summa lista = ', sum(list(range(1,11))))
# print('min', min(list(range(1,11))))
# print('max', max(list(range(1,11))))

# x = list(input())
# j = 0
# if len(x) == 19:
#     for i in x:
#         if i != ' ':
#             x[j] = int(i)
#             j += 1
# del x[10:]
# print(x)
# for i in range(5):
#     if x[i] == 2 and x[i] != x[i+1]:
#         del x[i]
# print(int((sum(x) / len(x)) // 1))

# events = list(range(2,21,2))
# average = sum(events) / len(events)
# print(average)
#
# x = ['r', 'o', 'y', 'g', 'b', 'i', 'v']
# x[3] = 'з'
# x[-1] = 'ф'
# print(x)

# x = list(range(1,11))
# x.reverse()
# print(x)
#
# x1 = [1,2,3]
# x2 = [6]
# x3 = list(range(7,14))
# print(x1*2 + x2*9 + x3)

# x = int(input('число пассажиров: '))
# h = int(input('Промежуток времени: '))
# o = 0
# for i in range(1, x+1):
#     z = input('время захода и выхода: ')
#     c = z.find(' ')
#     x1 = int(z[:c])
#     x2 = int(z[c+1:])
#     if x1 <= h <= x2:
#         o += 1
# print(o)

# x = [8,9,10,11]
# x1 = [4,5,6]
# x.extend(x1)
# del x[0]
# x = x*2
# x.insert(3,25)
# print(x)

# x = list(input())
# print(x.index(min(x)))
# print(x.index(max(x)))
