#using while loop
import random
#set max lives
lives = 5
#get random number
temp = random.randint(0,100)
#display remaining lives
print("Remanining lives: " + str(lives))

#run the game until the lives reached 0
x = input("Guess the number: ")
while lives > 0:
    x = int(x)
    if x != temp and lives!=0:
        lives = lives-1
        print("Remanining lives: " + str(lives))
        if x > temp:
            print("lower")
        elif x < temp:
            print("higher")
        x = input("Try Again: ")
    elif lives == 0:
        print("Game over! the hidden number is " + str(temp))
    else:
        print("You guessed it with " + str(lives) +" remaining")
print("Game over! the hidden number is " + str(temp))
        