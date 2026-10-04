# piramid

# 12 You are given three integers l, r, and k.
# Find how many numbers between l and r (including both l and r) are divisible by k.
# You only need to find the count, not print the numbers.

# l = 1
# r = 10
# k = 2
#
# count = 0
#
# for i in range(l, r + 1):
#     if i % k == 0:
#         count = count + 1
#
# print(count)

# data = '1 10 2 '
# newdata = data.strip()
# new = newdata.split()
# print(new)

# l = int(new[0])
# r = int(new[1])
# k = int(new[2])
#
# count = 0
#
# for i in range(l, r + 1):
#     if i % k == 0:
#         count = count + 1
#
# print(count)

# H
# for i in range(1, 6):
#     for j in range(1, 6):
#         if j == 1 or j == 5 or i == 3:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# A
# for i in range(1, 6):
#     for j in range(1, 6):
#          if j == 1 or j == 5 or i == 1 or i == 3:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# I
# for i in range(1, 6):
#     for j in range(1, 6):
#         if i == 1 or i == 5 or j == 3:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# S
# for i in range(1, 6):
#     for j in range(1, 6):
#         if i == 1 or i == 3 or i == 5 or (j == 1 and i == 2) or (j == 5 and i == 4):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# for i in range(1, 6):
#         for j in range(1, 6):
#             if i == 1 or i == 3 or i == 5:
#                 print("*", end=" ")
#             elif i == 2 and j == 1:
#                 print("*", end=" ")
#             elif i == 4 and j == 5:
#                 print("*", end=" ")
#             else:
#                 print(" ", end=" ")
#         print()

for i in range(1,7):
    for j in range(1,7):
        if i ==5 or j==:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print('')

# consider column j and row i for easy
for i in range(1,6):
    for j in range(1,6):
        if i ==1 or i==5 or j==3:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print('')

for i in range(1, 6):
    for j in range(1, 6):
        if i == 1 or i == 3 or i == 5 or (i == 2 and j == 1) or (i == 4 and j == 5):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print("")

for i in range(1, 7):
    for j in range(1, 6):
        if (i == 1 and j > 1) or (i == 2 and j == 1) or (i == 3 and j > 1 and j < 5) or (i == 4 and j == 5) or (i == 5 and j < 5):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print("")

# sum(10)
# = 10 + sum(9)
# = 10 + 9 + sum(8)
# = 10 + 9 + 8 + sum(7)
# ...
# = 10 + 9 + 8 + ... + 1 + sum(0)

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)
#
# print(factorial(5))

# How this works :

# 5 × factorial(4)
#
# 5 × 4 × factorial(3)
#
# 5 × 4 × 3 × factorial(2)
#
# 5 × 4 × 3 × 2 × factorial(1)
#
# 5 × 4 × 3 × 2 × 1 × factorial(0)

num = 1

for i in range(1, 6):
    for j in range(1, i + 1):
        print(num, end=" ")
        num += 1

