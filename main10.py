# result = 0
# for i in range(10):
#     if i % 2 == 0:
#         continue
#     result += i
# print(result)

# mult = 1
# for i in range(1, 11):
#    if i % 2 == 0:
#       continue
#    if i % 9 == 0:
#       break
#    mult *= i
# print(mult)

# x = int(input())
# z = 1
# while x > z:
#     z += 1
#     if x % z == 0:
#         v = z
#         print(v)

# x = int(input())
# for i in range(1, x+1):
#     if 5 <= i <= 9:
#         continue
#     if 17 <= i <= 37:
#         continue
#     if 78 <= i <= 87:
#         continue
#     print(i)

# for i in range(1, 101):
#     if i == 7 or i == 27or i == 29 or i == 78:
#         continue
#     print(i)

# for i in range(10):
#     print(i, end = '*')
#     if i > 6:
#         break

# x = int(input())
# y = int(input())
# z = 1
# while x > 0 and y > 0:
#     z += 1
#     if z % x == 0 and z % y == 0:
#         break
# print(z)

# x = int(input())
# y = int(input())
# z = 1
# while x > 0 and y > 0:
#     z += 1
#     if x % z == 0 and y % z == 0:
#         break
# print(z)

# x = 5
#
# for y in range(x, 0, -1):
#     print(' ' * (x - y), end='')
#     for c in range(2 * y - 1):
#         if c == 0 or c == 2 * y - 2 or y == x:
#             print('*', end='')
#         else:
#             print(' ', end='')
#     print()
#
# for y in range(2, x + 1):
#     print(' ' * (x - y), end='')
#     for c in range(2 * y - 1):
#         if c == 0 or c == 2 * y - 2 or y == x:
#             print('*', end='')
#         else:
#             print(' ', end='')
#     print()
num = int(input())
total = 0
counter = 0
while num != -1:
    if num > 7:
        total += num
        counter += 1
    num = int(input())
print(total / counter)

