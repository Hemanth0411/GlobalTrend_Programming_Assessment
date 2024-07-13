num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operator = input("Enter the operation to be performed(+,-,*,/): ")
if operator == '+':
  result = num1 + num2
elif operator == '-':
  result = num1 - num2
elif operator == '*':
  result = num1 * num2
elif operator == '/':
  result = num1 / num2

print(f"{num1} {operator} {num2} = {result}")
