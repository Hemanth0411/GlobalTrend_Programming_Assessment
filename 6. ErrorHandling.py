num1 = int(input("Enter the dividend: "))
num2 = int(input("Enter the divisor: "))

try:
  print(f"{num1} / {num2} = {num1/num2}")
except ZeroDivisionError:
  print("\nDivision by zero is not possible.")
