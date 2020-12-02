def addition(x, y):
    return x + y


def subtraction(x, y):
    return x - y


def multiplication(x, y):
    return x * y


def division(x, y):
    return x / y


operator = None

print("Select operator:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplicaton")
print("4. Division")

operator = int(input)

if operator == "1":
    print("Addition selected.")
elif operator == "2":
    print("Subtraction selected.")
elif operator == "3":
    print("Division selected.")
elif operator == "4":
    print("Multiplication selected.")
else:
    print("Unknown operator. \n")

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

if operator == "1":
    print(x, "+", y, "=", addition(x, y))
elif operator == "2":
    print(x, "-", y, "=", subtraction(x, y))
elif operator == "3":
    print(x, "*", y, "=", multiplication(x, y))
elif operator == "4":
    print(x, "/", y, "=", division(x, y))
