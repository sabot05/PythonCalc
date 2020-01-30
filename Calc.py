# Calculator ver.1

sign = input("Select action (+, -, *, /)")

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if sign == "+":
    c = a + b
    print("result: " + str (c))
elif sign == "-":
    c = a - b
    print("result: " + str(c))
