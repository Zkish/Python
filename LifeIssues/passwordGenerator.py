import random

# defining password parameters
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o','p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10','!', '@', '#', '$', '%', '^', '&', '*']

# length of password
lengthOfPassword = 5 # length of password divided by 2 to get desired length.

# random choices for password to use
letterPart = random.choice(letters)
numberPart = random.choice(numbers)

# takes a random sample from the letterpart and number part to be used, both will push out 5 random characters from both letters and number parts of the password
letters = random.sample(letters, lengthOfPassword)
numbers = random.sample(numbers, lengthOfPassword)

# combining together to get password
password = letters + numbers

# output
print(password)
exit()