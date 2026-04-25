
import numpy as np
import matplotlib.pyplot as plt

# Create a sample 100x100 2D array
array = np.random.rand(100, 100)

# Define the center and angle
center = (50, 50)
angle = 25  # degrees

# Convert angle to radians
rad = np.radians(angle)

# Calculate slope
slope = np.tan(rad)

# Generate coordinates for cross profile
length = 50  # Extend profile length
x_positive = np.arange(center[1] - length, center[1] + length + 1)
y_positive = center[0] + slope * (x_positive - center[1])

x_negative = np.arange(center[1] - length, center[1] + length + 1)
y_negative = center[0] - slope * (x_negative - center[1])

# Filter valid coordinates within the array bounds
valid_positive = [(int(y), int(x)) for x, y in zip(x_positive, y_positive) if 0 <= y < 100 and 0 <= x < 100]
valid_negative = [(int(y), int(x)) for x, y in zip(x_negative, y_negative) if 0 <= y < 100 and 0 <= x < 100]

# Extract values from the array
cross_profile = [array[y, x] for y, x in valid_positive + valid_negative]

print("Cross Profile Values:", cross_profile)

# Optional: Visualize the cross profile
plt.imshow(array, cmap='gray')
for (y, x) in valid_positive + valid_negative:
    plt.plot(x, y, 'r.', markersize=5)
plt.scatter(center[1], center[0], color='blue', label='Center', s=50)
plt.legend()
plt.title('Cross Profile Visualization')
plt.show()
