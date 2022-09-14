#functions
def add(a,c):
    temp = a + c
    return temp

def sub(a,c):
    temp = a - c
    return temp

def mul(a,c):
    temp = a * c
    return temp

def div(a,c):
    temp = a / c
    return temp

#main program on loop
ans = "y"
while ans != "n":
    a = input("Enter first number: ")
    b = input("Enter Operator: ")
    c = input("Enter second number: ")

    error= 0

    if a.isnumeric():
       a = float(a)
    else:
        error += 1

    if c.isnumeric():
      c = float(c)
    else:
        error += 1

    if error == 0:
     if b == "+":
      x = add(a,c)
      print("The total is " + str(x))
     elif b == "-":
      x = sub(a,c)
      print("The difference is " + str(x))
     elif b == "*" or b == "x":
      x = mul(a,c)
      print("The product is " + str(x))   
     elif b == "/":
      x = div(a,c)
      print("The quotient is " + str(x))
     else:
      print("Invalid operator")
    else:
        print("NaN")
    error = 0
    ans = input("another(y,n)? ")

