# Fibonacci number series using recursion in github add
def counttozeroo(n):
    if n <=1:
        return n
    else:
        return counttozeroo(n-1) + counttozeroo(n-2)
num_terms = 10
if num_terms <= 0:
    print("Please enter a positive integer.")
else:
    print(f"Fibonacci series ({num_terms} terms):")
    for i in range(num_terms):
        print(counttozeroo(i), end=" ")