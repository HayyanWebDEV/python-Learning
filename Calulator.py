
print("This is a calculator program")
operator = input("Enter the operator (+,-,x,/): ")
number_a = float(input("Enter a number: "))
number_b = float(input("Enter another number: "))
print("")
if operator == "+":
    result = number_a + number_b
elif operator == "-":
    result = number_a - number_b
elif operator == "x":
    result = number_a * number_b
elif operator == "/":
    result = number_a / number_b
else:
    print("Invalid operator")

print(round(result,3))