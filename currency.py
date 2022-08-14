a = input("How many do you have left in yuan?")
b = input("How many do you have left in yen?")
c = input("How many do you have left in won?")

convert1 = int(a) * 0.15
convert2 = int(b) * 0.0075
convert3 = int(c) * 0.00077

total = convert1+convert2+convert3

print("Total Amount Converted:" + str(total))