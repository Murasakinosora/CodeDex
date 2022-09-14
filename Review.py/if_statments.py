from random import random
import random


def test1():
    vip = ["Yes"]
    list = ["Dragon"]
    visitor = input("Input Name: ")
    if visitor in vip:
     print("Welcome!")
    elif visitor in list:
        print("Please register!")
    else:
        print("Please Leave")

def test2():
    a = 0
    while a!=10:
     x = random.randint(0,100)
     if 50>x>30:
        print("Winner")
     else:
        print("Try again")
     a+=1

#With comparisons

def chances(p1,p2,p3):
    if p1 > p2 and p1 > p3:
        print("p1 is the winner: " + str(p1))
    elif p2 > p1 and p2 > p3:
        print("p2 is the winner: " + str(p2))
    elif p3 > p2 and p3 > p1:
        print("p3 is the winner: " + str(p3))

chances(random.randint(0,1000),random.randint(0,1000),random.randint(0,1000))