import random

choices = ["rock", "paper", "scissors",]

randomChoice = random.choice(choices)

userSelection = input("rock, paper, or scissors: ")

# losing selections
while userSelection == "paper" and randomChoice == "scissors":
    print("you lost to the randomizer")
    print(userSelection, "loses to ", randomChoice)
    break
while userSelection == "scissors" and randomChoice == "rock":
    print("you lost to the randomizer")
    print(userSelection, "loses to ", randomChoice)
    break
while userSelection == "rock" and randomChoice == "paper":
    print("you lost to the randomizer")
    print(userSelection, "loses to ", randomChoice)
    break

# winning selections
while userSelection == "scissors" and randomChoice == "paper":
    print("you won to the randomizer")
    print(userSelection, "beats ", randomChoice)
    break
while userSelection == "rock" and randomChoice == "scissors":
    print("you won to the randomizer")
    print(userSelection, "beats", randomChoice)
    break
while userSelection == "paper" and randomChoice == "rock":
    print("you won to the randomizer")
    print(userSelection, "beats", randomChoice)
    break