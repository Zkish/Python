import random
i = random.randint(1, 10)
while True:
    Guess = int(input("Pick a Number 1 - 10: "))
    if Guess == i:
        print("You are a Winner!!!")
        exit()
    else:
        print("Your a Loser.")
        print("The Number Was: ", i)