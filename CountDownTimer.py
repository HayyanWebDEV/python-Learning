import time

sec =  int(input("Enter the amount of time seconds: "))
min = int(input("Enter the amount of time minutes: "))
hrs = int(input("Enter the amount of time hours: "))

Time = sec + (min * 60) + (hrs * 3600)

for i in range( Time , 0 ,-1 ):
    seconds = i % 60
    minutes = int(i / 60 ) % 60
    hours = int(i / 3600 )
    print(f"  {hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print(f'Times Up! After {hrs} Hours, {min} Minutes, {sec} Seconds.')