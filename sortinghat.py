Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0

def house(a,b,c,d):
    if b<a>c and a>d:
        print("You are Assigned to Gryffindor!")
    elif a<b>c and b>d:
        print("You are Assigned to Ravenclaw!")
    elif a<c>b and c>d:
        print("You are Assigned to Hufflepuff!")
    elif a<d>b and d>c:
        print("Your are Assigned to Slytherin")
    else:
        print(str(Gryffindor) + str(Ravenclaw) + str(Hufflepuff) + str(Slytherin) )


q1 = input("Q1) Do you like Dawn or Dusk?\n 1)Dawn \n 2)Dusk\n - ")

if q1 == "1":
    Gryffindor += 1
    Ravenclaw += 1
elif q1 == "2":
    Hufflepuff += 1
    Slytherin += 1
else:
    print("Wrong input")

q2 = input("Q2) When I’m dead, I want people to remember me as: \n   1)The Good\n   2)The Great"
+"\n   3)The Wise \n   4)The Bold\n -")

if q2 == "1":
    Hufflepuff += 1
elif q2 == "2":
    Slytherin += 1
elif q2 =="3":
    Ravenclaw += 1
elif q2 == "4":
    Gryffindor += 1
else:
    "Wrong input"

q3 = input("Q3) Which kind of instrument most pleases your ear?"+
    "\n    1) The violin"
    "\n    2) The trumpet"
    "\n    3) The piano"
    "\n    4) The drum\n -")

if q3 == "2":
    Hufflepuff += 1
elif q3 == "1":
    Slytherin += 1
elif q3 =="3":
    Ravenclaw += 1
elif q3 == "4":
    Gryffindor += 1
else:
    "Wrong input"

house(Gryffindor,Ravenclaw,Hufflepuff,Slytherin)

