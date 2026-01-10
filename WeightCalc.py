  # This is Python Weight Converter
  # print(help(str))
weight = float(input("Enter Weight: "))
unit = input("Enter Unit(kg or lb): ")

if unit == "Kg" or unit == "kg":
       weight = weight * 2.205
       unit = "lbs"
elif unit == "lb" or unit == "lb":
       weight = weight / 2.205
       unit = "kgs"
else:
       print(f"{unit} is Invalid unit")
       exit()


weight = round(weight,2)
print(f"Your W8 is {weight} {unit}")

