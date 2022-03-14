# Jednoduchý príklad rekurzie
def do_recursion(number):
    print("Number is: ", number)
    if number > 0:
        do_recursion(number - 1)
do_recursion(20)


# vráti súčet prvých celých čísel
def sum_recursion(number):
    
    if number == 0:
        return 0
    return number + sum_recursion(number - 1)

print(sum_recursion(15))

# vráti faktoriál
def factorial(number):

    if number == 0:
        return 1

    return number * factorial(number - 1)

# print(factorial(15))


# Fibonacciho postupnosť
def fibonacci(number):
    if number == 1:
        return 0 
    if number == 2:
        return 1
    else:
        return fibonacci(number-1) + fibonacci(number -2)
      
print(fibonacci(15))

