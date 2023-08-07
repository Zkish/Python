# imports needed:
import matplotlib.pyplot as plt
import numpy as np
import random

# coordinates
a = (1, 10) 
b = (1, 10)

# the graph
plt.xlabel("distance")
plt.ylabel("speed")
# to get different graphs try to do plt.bar(x, y) or scatter or whichever graph you would need to use.
plt.plot(a, b)
plt.show()