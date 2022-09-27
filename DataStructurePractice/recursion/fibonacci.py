#Fibonacci series is a series where first no. is 1 and
#second 1 and then all the further number will be addtion of 
#previous number

def fib(n):
    if n <=1 :
        return n 
    else:
        return (fib(n-1) + fib(n-2))

count = 6
if count <= 0:
    print("Please enter the value more than 1")
else:
    sum = 0
    for i in range(count):
        # to ge the sum of fibonnaci series
        sum = sum +fib(i)
        lastValue = fib(i)
    # if interview ask that I need a 6 value
    print(lastValue)
    print(sum)

 


