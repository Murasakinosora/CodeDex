#creating a function

def sample_function():
    print("Working sample")

#calling
sample_function()

#function with a parameter

def add(a, b):
    c = int(a) + int(b)
    print(c)

a = 2
b = 3

#calling with two different methods
add(a,b)
add(5,7)

#calling with return

def ret(a,b,c):
    total = int(a) + int(b) * int(c)
    total = str(total)
    return total

tempq = ret(10,20,30)

print("Your total is: " + tempq)

def sqr(a):
    return int(a)**0.5

print(sqr(20))
