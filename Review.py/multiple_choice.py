from questions1 import question_holder

prompt=[
    "What color is the sky?\n a) Red   b) Green \nc)blue    d)yellow",
    "What color is the grass?\n a) Red   b) Green \nc)blue    d)yellow"
]
#creating an object with the question_holder class
questions = [
    #passing the contents of prompt onto the class
    question_holder(prompt[0],"c"),
    question_holder(prompt[1],"b")
]

def test(questions):
    score = 0
    #accessing the objects using for loop
    for question in questions:
     print(question.prompt)
     x = input("Type in your answer: ")
     if x == question.answer:
        score +=1
    print("Your score is: " + str(score))

test(questions)