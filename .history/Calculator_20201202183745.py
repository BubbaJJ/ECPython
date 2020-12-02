def addition(x, y):
    return x + y


def subtraction(x, y):
    return x - y


def multiplication(x, y):
    return x * y


def division(x, y):
    return x / y


operator = None
result = None

print("Select operator:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplicaton")
print("4. Division")

operator = int(input())

if operator == 1:
    print("Addition selected.")
elif operator == 2:
    print("Subtraction selected.")
elif operator == 3:
    print("Division selected.")
elif operator == 4:
    print("Multiplication selected.")
else:
    print("Unknown operator. \n")

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

if operator == 1:
    result = addition(x, y)
    print(x, "+", y, "=", addition(x, y))
elif operator == 2:
    result = subtraction(x, y)
    print(x, "-", y, "=", subtraction(x, y))
elif operator == 3:
    result = multiplication(x, y)
    print(x, "*", y, "=", multiplication(x, y))
elif operator == 4:
    result = division(x, y)
    print(x, "/", y, "=", division(x, y))

if result > 0 and result < 101:
    if result == 100:
        print("Spot on!")
    elif result == 50:
        print("Fifty!")
    elif result > 0 and result < 50:
        print("Less then fifty")
    elif result > 50 and result < 100:
        print("Almost a hundred")
    elif result > 100:
        print("Missed the spot!")
else:
    print("Not really sure what you doing....")
