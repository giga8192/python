def fact(x):
    result = 1
    if x == 0:
        return result
    for num in range(1, x + 1):
        result *= num
    return result

def fizzbuzz(x):
    result = str(x)
    if x % 3 == 0 and x % 5 == 0:
        result = 'FizzBuzz'
    elif x % 3 == 0:
        result = 'Fizz'
    elif x % 5 == 0:
        result = 'Buzz'
    return result

def fib(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    return fib(x - 1) + fib(x - 2)

PI = 3.14159
