# print all the prime numbers within a limit.
# (Limit - 10-100)

count = 0
for num in range(10,101):
    if num > 1:
        for i in range(2,num):
            if num % i == 0:
                break
        else:
            print(num, end=" ")
            count = count + 1
print("\nThere are", count ," prime numbers in this range.")