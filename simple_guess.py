import random
tries = 0
x = random.randint(0,6)
guess = 0
while guess != x and tries<6:
     guess = int(input("Guess the number: "))
     tries += 1
print("You guessed the number : " + str(x))