#imports
import random
# selecting character stats
# starting stat points
statpoints = 24
# starting actual selection of stats
print("pick your characters skill abilities max skill is 10 and you only have 24 points to use")
strength = int(input("characters strength ability: "))
statpoints = statpoints - strength
print("points you have left are: ", statpoints)
perception = int(input("characters percepton ability: "))
statpoints = statpoints - perception
print("points you have left are: ", statpoints)
endurance = int(input("characters endurance ability: "))
statpoints = statpoints - endurance
print("points you have left are: ", statpoints)
charisma = int(input("characters charismatic ability: "))
statpoints = statpoints - charisma
print("points you have left are: ", statpoints)
intelligence = int(input("characters intelligence ability: "))
statpoints = statpoints - intelligence
print("points you have left are: ", statpoints)
agility = int(input("characters agility ability: "))
statpoints = statpoints - agility
print("points you have left are: ", statpoints)
luck = int(input("characters luck ability: "))
statpoints = statpoints - luck
print("points you have left are: ", statpoints)
# error handling
if statpoints < 0:
    exit()
# show final stats
characterStats = strength, perception, endurance, charisma, intelligence,agility,luck
print(" S ", "P ", "E ", "C ", "I ", "A ", "L ")
print(characterStats)
print("\n")
# into the actual world
print("You Wander into the vast wasteland of Pittsburgh emerging from your shelter 78 days after the bombs fell")
print("do you want to scavenge your house for items before traveling onwards?")
onwards = input("(y,n)")
if onwards == "y":
    encounters = ["wounded dog", "raider"]
    actualEncounter = random.choice(encounters)
    print("you scavenge your house in search of finding some useful items")
    print("along your journey out into the wasteland you ecounter a ", actualEncounter, "do you investigate further or go a seperate direction?")
    encounterchoice = input("investigate, move: ")
    if actualEncounter == "wounded dog" and encounterchoice == "investigate":
        print("would you like to heal the wounded dog?")
        dogchoice = input("y/n: ")
elif onwards == "n":
    print("you go into the vast wasteland in search of items and your destiny")