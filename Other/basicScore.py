import random
number = random.randint(1, 10)
guesses = 0
while True:
    guess = int(input("take a guess: "))
    guesses += 1
    if guess == number:
        print("CONGRADULATIONS YOU GUESSES IT YOUR A WINNER it took you ", guesses, " guesses to get it right")
        exit()
    else:
        print("loser youve made ", guesses, "attempts at getting this correct and lost")