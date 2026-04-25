
import numpy as np
import matplotlib.pyplot as plt

def extract_cross_profile(array, center, angle_degrees, length=50):
    angle_radians = np.radians(angle_degrees)
    x0, y0 = center
    half_length = length // 2

    # Create coordinates for the cross profile
    x = np.linspace(-half_length, half_length, length)
    y1 = y0 + np.tan(angle_radians) * x  # Diagonal line 1
    y2 = y0 - np.tan(angle_radians) * x  # Diagonal line 2

    # Collect values ensuring we stay within array bounds
    profile1 = [array[int(np.clip(y1i, 0, array.shape[0]-1)), int(np.clip(xi + x0, 0, array.shape[1]-1))] for xi, y1i in zip(x, y1)]
    profile2 = [array[int(np.clip(y2i, 0, array.shape[0]-1)), int(np.clip(xi + x0, 0, array.shape[1]-1))] for xi, y2i in zip(x, y2)]

    return np.array(profile1), np.array(profile2)

# Example usage
array = np.random.rand(100, 100)  # Creating a 100x100 random array
center = (50, 50)
angle = 25

profile1, profile2 = extract_cross_profile(array, center, angle)

# Plot the profiles for visualization
plt.figure(figsize=(10, 5))
plt.plot(profile1, label='Profile at +25°')
plt.plot(profile2, label='Profile at -25°')
plt.title('Diagonal Cross Profile')
plt.xlabel('Position along the cross profile')
plt.ylabel('Values')
plt.legend()
plt.show()
