
def myfact(n):
    if n == 1:
        return n
    else:
        return n * myfact(n-1)


num = 5

if num < 0:
    print("No negative numbers")
elif num == 0:
    print("Factorial is: 1")
else:
    print("Factorial is: ", myfact(num))