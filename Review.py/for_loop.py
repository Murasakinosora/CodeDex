#for loop example

#traversing through every letter
#letter holds the value of the letters in each loop

#for letter in "Giraffe Academy":
 #   print(letter)

sample = ["sun","moon","earth"]

#prints 0-9 , can also be range(10)
for index in range(3,10):
    print(index)

#using the length of an array as the value for range

for index in range(len(sample)):
    print(sample[index])

#conditional

for index in range(10):
    if index%2 == 1:
        print("not odd")
    else:
        print("even")