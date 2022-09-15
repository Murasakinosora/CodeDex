vowels = ["a","e","i","o","u"]


#vowels in the if statement can also be implemented as "AEIOUaeiou" instead of an array
def translate(word):
    final=""
    for letter in word:
        if letter.lower() in vowels:
            if letter.isupper():
             letter = "Q"
             final+=letter
            else:
             letter = "q"
             final+=letter
        else:
            final+=letter
    return final


print(translate(input("Enter a word: ")))