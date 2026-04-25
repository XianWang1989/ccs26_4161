
import numpy as np
import matplotlib.pyplot as plt

def extract_cross_profile(array, center, angle_degrees, length):
    angle_radians = np.radians(angle_degrees)
    half_length = length / 2

    # Compute the offsets from center
    x_offset = np.arange(-half_length, half_length+1)
    y_offset = np.tan(angle_radians) * x_offset

    # Calculate the diagonal points
    x_points = np.clip(center[0] + x_offset, 0, array.shape[1]-1)
    y_points = np.clip(center[1] + y_offset, 0, array.shape[0]-1)

    # Retrieve the values from the array
    return array[y_points.astype(int), x_points.astype(int)]

# Example usage
array = np.random.rand(100, 100)
center = (50, 50)
angle = 25
length = 40

cross_profile = extract_cross_profile(array, center, angle, length)

# Visualize the original array and the extracted cross profile
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(array, cmap='gray')
plt.title('Original Array')

plt.subplot(1, 2, 2)
plt.plot(cross_profile)
plt.title('Cross Profile at Angle {}°'.format(angle))
plt.xlabel('Position along the line')
plt.ylabel('Value')
plt.grid()
plt.show()
