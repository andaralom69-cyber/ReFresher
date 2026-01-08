# for s in range(24):
#     for a in range(60):
#         for d in range(60):
#             print(s, a, d)

# for i in range(3):
#     for j in range(3):
#         if i == j:
#             continue
#         print(i, j)

# x = int(input())
# if x <= 9:
#     for f in range(x):
#         for i in range(3):
#             print(x, end=' ')
#         print()
# else:
#     print('err')

# x = int(input())
# if x <= 9:
#     for f in range(x):
#         for i in range(1, 5):
#             print(f + 1, end=' ')
#         print()
# else:
#     print('err')

# x = int(input())
# if x <= 9:
#     for f in range(1, x+1):
#         for i in range(1, 10):
#             temp = i + f
#             print(f, '+', i, '=', temp)
#         print()
# else:
#     print('err')

# n = int(input())
# mid = (n + 1) // 2
# if n % 2 != 0:
#     for i in range(1, mid + 1):
#         for j in range(i):
#             print('*', end='')
#         print()
#     for i in range(mid - 1, 0, -1):
#         for j in range(i):
#             print('*', end='')
#         print()
# else:
#     print('err')

x = int(input())
m = 1
for i in range(1, x + 1):
    for g in range(1, i+1):
        print(m, end='')
    print()
    m += 1

# x = int(input())
# ser = int(x // 2)
# for i in range(1, ser + 2):
#     for g in range(i):
#         print('*' * g, end='')
#     print()
# for i in range(ser, 0, -1):
#     for g in range(i+1):
#         print('*' * g, end='')
#     print()

# n = 5
# for i in range(1, n // 2 + 2):
#     for j in range(i):
#         print("*", end="")
#     print()
# for i in range(n // 2, 0, -1):
#     for j in range(i):
#         print("*", end="")
#     print()