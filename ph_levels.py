ph = input("Enter pH level (0-14): ")
ph = int(ph)
if ph > 7:
    print("Basic")
elif ph < 7:
    print("acidic")
else:
    print("Neutral")