import random

worldchoices = ["No sea Life", "has water", "no water", "has sea life", "has land life", "no land life", "mountains", "mostly flat"]
worldMakeup = 4
ActualWorld = random.sample(worldchoices, worldMakeup)

print(ActualWorld)