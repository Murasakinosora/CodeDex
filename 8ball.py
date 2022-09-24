import random

x = ["Yes - definitely","It is decidedly so",
"Without a doubt.","Reply hazy, try again.",
"Ask again later.","Better not tell you now",
"My sources say no.",
"Outlook not so good.","Very doubtful."]

index = random.randint(0,8)
answer = input("Question: ")

print("Magic 8 ball: " + x[index])