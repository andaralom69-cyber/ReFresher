# def a(x1, x2, y1, y2):
#     x3 = (x1 + x2) / 2
#     y3 = (y1 + y2) / 2
#     return y3, x3
# x1, x2 = int(input()),int(input())
# y1, y2 = int(input()),int(input())
# print(a(x1,x2,y1,y2))

# def a(x, y):
#     d = list()
#     for i in x:
#         if i == y:
#             j = x.find(y)
#             d.append(j)
#             del x[j]
#     return d
# x, y = input(), input()
# print(a(x, y))

def dedede(x):
    if x == str(x):
        print(x, ' - это строка.')
    elif x == int(x):
        print(x * x, ' - ваше введное число это сторона квадрата, а это его площадь.')
    elif x == float(x):
        result = (5 / 9) * (x - 32)
        print(x, ' градусов по фаренгейту - это ',result, ' градусов цельсия.')
dedede(200.54)
