# this is Python compound interest Calculator

principle = 0
rate = 0
time = 0
while principle <= 0:
     principle = float(input("Enter principle amount pkr: "))
     if principle <= 0:
         print("Principle amount must be greater than 0pkr")

while rate <= 0:
    rate = float(input("Enter rate %: "))
    if rate <= 0:
        print("Rate amount must be greater than 0%")
    elif rate >= 51:
        print("Rate amount Can not be greater than 50%")
        rate = 0

while time <= 0:
    time = float(input("Enter time years: "))
    if time <= 0:
        print("Time amount must be greater than 0s")

total = principle * pow((1 + rate / 100), time)
print(f"Your Balance: {principle}pkr After {time} year/s total amount is {total:.2f}pkr")