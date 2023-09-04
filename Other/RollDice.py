import random

sides = int(input("how many sides do you want the dice to have: "))
print("your dice has ", sides, " sides")

while True:
    diceroll = random.randint(1, sides)
    print("would you like to roll the dice?")
    again = input("y/n: ")
    if again == "y":
        print(diceroll)
    elif again == "n":
        exit()