# Program to print all prime numbers within a limit

limit = int(input("Please enter the limit: "))

for num in range(2, limit + 1):
    count = 0

    for i in range(1, num + 1):
        if num % i == 0:
            count = count + 1

    if count == 2:
        print(num)