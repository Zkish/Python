import random

worldTerrain = ["rugged", "flat"]
worldLifeWater = ["no sea life", "has sea life"]
worldLifeLand = ["no land life", "has land life"]
worldTemperature = ["hot", "very hot", "cold", "very cold"]

sampler = 1
Terrain = random.sample(worldTerrain, sampler)
Water = random.sample(worldLifeWater, sampler)
Land = random.sample(worldLifeLand, sampler)
Temperature = random.sample(worldTemperature, sampler)

world = Terrain + Temperature + Water + Land

print(world)

