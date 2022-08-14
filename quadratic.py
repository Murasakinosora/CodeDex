from cmath import sqrt


a = int(input("Enter a whole number for a:"))
b = int(input("Enter a whole number for b:"))
c = int(input("Enter a whole number for c:"))


if(a!=None and b!=None and c!=None):

 s = pow(b,2)
 x1 = (-b + ( s - 4*a*c)**0.5) / (2*a)
 x2 = (-b - ( s - 4*a*c)**0.5) / (2*a)
 print(x1)
 print(x2)