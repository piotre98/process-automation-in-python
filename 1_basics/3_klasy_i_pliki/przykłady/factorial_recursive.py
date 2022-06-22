# Factorial of a number using recursion

def recursive_factorial(number: int):
    if number in [0, 1]:
        return 1
    else:
        return number * recursive_factorial(number - 1)

#factorial(factorial(factorial(factorial(4))

n = int(input("State n for factorial number: "))
if n < 0:
    print("Sorry, factorial does not exist for negative numbers")
else:
    print(f"The factorial of {n} is {recursive_factorial(n)}")
