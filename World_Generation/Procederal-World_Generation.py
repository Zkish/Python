import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage.filters import gaussian_filter

# Set the seed for reproducibility leave empty for randomization
np.random.seed()

# Generate a random noise map
world_size = (1024, 1024)
noise = np.random.rand(*world_size)

# Apply Gaussian blur to make the noise smoother, simulating terrain features
smoothed_noise = gaussian_filter(noise, sigma=50)

# Create elevation levels for different terrain types
sea_level = 0.3
beach_level = 0.35
forest_level = 0.5
mountain_level = 0.7

# Assign colors to each elevation level
world_map = np.zeros((*world_size, 3))
world_map[smoothed_noise <= sea_level] = [0.1, 0.5, 1]   # Deep water
world_map[(smoothed_noise > sea_level) & (smoothed_noise <= beach_level)] = [0.9, 0.9, 0.6] # Beach
world_map[(smoothed_noise > beach_level) & (smoothed_noise <= forest_level)] = [0.2, 0.6, 0.2] # Forest
world_map[(smoothed_noise > forest_level) & (smoothed_noise <= mountain_level)] = [0.5, 0.5, 0.5] # Mountains
world_map[smoothed_noise > mountain_level] = [1, 1, 1] # Snow peaks

plt.figure(figsize=(10, 10))
plt.imshow(world_map)
plt.axis('off') # Hide axes
plt.show()