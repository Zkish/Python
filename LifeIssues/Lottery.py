import random
# arrays to store numbers and powerball of lottery
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 
        11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
        21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 
        31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 
        41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 
        51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
        61, 62, 63, 64, 65, 66, 67, 68, 69]

powerball = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 
             11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 
             21, 22, 23, 24, 25, 26]
# gets the random numbers from lottery and powerball
picker = 5
numbersDrew = random.sample(numbers, picker)
powerball = random.choice(powerball)
# selecting user numbers
for i in range(5):
    Usernumbers = int(input("pick a number for the lottery: "))
    continue
userPowerball = int(input("Pick Your Powerball For The Lottery:\n"))
# did the user win or not
if Usernumbers == numbersDrew:
    print("YOU WON THE LOTTERY")
else:
    print("YOU LOST THE LOTTERY\n", "The Winning Numbers Were\n", numbersDrew)

if userPowerball == powerball:
        print("YOU WON THE POWERBALL")
else:
    if userPowerball != powerball:
        print(" YOU LOST THE POWERBALL\n", "The Powerball was: ", powerball)