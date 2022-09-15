
try:
 value = 5/0   
 number = int(input("Enter a number"))
 print(number)
 #put ZeroDivision error to ignore this exception
except ZeroDivisionError:
    print("divided by 0")
except ValueError:
    print("Invalid input")

#always put specific errors to catch