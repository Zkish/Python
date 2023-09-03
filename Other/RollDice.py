import random as random

dice = random.randint(1, 6)
print("The number you rolled is:\n", dice)

while True:
    again = input("would you like to roll again? (y/n): ")
    if again == "y":
        dice = random.randint(1, 6)
        print("The number you rolled is:\n", dice)
        continue
    else:
        exit()