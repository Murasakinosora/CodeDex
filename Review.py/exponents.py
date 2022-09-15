def exponents(base,exp):
   result=1
   for index in range(exp):
       result = result * base
   return result

print(exponents(2,8))