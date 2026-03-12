#iterating  functions
def r_function(steps) :
    for step in range(1 ,steps+1) :
        symbol = {1: "st" , 2: "nd" , 3: "rd"}.get(step % 10 , "th")
        print(f"{step}{symbol} step")

r_function(10)

print("")
print("--------------------------------------------------------")
print("")

def factorial_function(n):
    result = 1
    for n in range(1,n+1):
        result = result * n
        print(result)

factorial_function(10)

print("")
print("--------------------------------------------------------")
print("")

def fabonacci_function(n):
    if n < 2:
        return n
    else:
        return fabonacci_function(n-1) + fabonacci_function(n-2)

for i in range(15):
    print(i+1 ,fabonacci_function(i+1))