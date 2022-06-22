factorial = 1
n = int(input("State n for factorial number: "))

for i in range(1, n + 1):
    factorial *= i

print(f"The factorial of {n} is : {factorial=}")
