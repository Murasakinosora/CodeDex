string = "name"
integer = 2
bools  = True
bools1 = False

## Working with Strings

word = "Word"
##functions

print(word.upper())
print(word.lower())
print(word.islower())
print(word.isupper())

##combining

print(word.upper().isupper())

#length

print(len(word))

#Traversing per word 

print(word[3])

#Working with numbers

Num =-2

print(Num)

temp = str(Num)

print(type(temp))

#absolute value

print(abs(Num))

# operator

print(pow(abs(Num),5))

#returning the highes and lowest value respectively

print(max(Num,10))
print(min(Num,10))

#rounding = round(Num)

#additional math functions with library

from math import *

# returning floor value
print(floor(8.2))
# returning ceiling value
print(ceil(5.2))
#sqrt
print(sqrt(abs(Num)))