# Simple calculator 
print("Simple calculator")
num1 = float(input("Enter first number: "))
op = input("Enter operator (+, -, *, /)")
num2 = float(input("Enter second number: "))

if op == "+":
 print(f"Result: {num1 + num2}")
elif op == "_":
 print(f"Result: {num1 - num2}")
elif op == "*":
 print(f"Result: {num1 * num2}")
elif op == "/":
 if num2 != 0:
  print("Error: Division by zero.")
else:
 print("Invalid operator")