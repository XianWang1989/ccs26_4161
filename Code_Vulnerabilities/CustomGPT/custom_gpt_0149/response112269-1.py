
import numpy as np
import matplotlib.pyplot as plt

# Generate sample data
n_lines = 100
x = np.linspace(0, 10, 100)
y_data = [np.sin(x + np.random.uniform(0, 2 * np.pi)) + np.random.normal(0, 0.1, size=x.shape) for _ in range(n_lines)]

# Create a figure and axis
fig, ax = plt.subplots()

# Initialize a canvas for adding lines
canvas = np.zeros((100, 100))

# Loop through each line and draw it
for i in range(n_lines):
    y = y_data[i]
    # Normalize the data to fit the canvas size
    y_normalized = ((y - y.min()) / (y.max() - y.min()) * 99).astype(int)
    for j in range(len(x)):
        if 0 <= y_normalized[j] < 100:
            canvas[y_normalized[j], int(x[j] % 100)] += 1  # Increment pixel value

# Plot the blended result as an image
ax.imshow(canvas, extent=[0, 10, -2, 2], origin='lower', cmap='Greys', interpolation='nearest')
ax.set_title('2D Density Plot with Distinct Lines')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')

plt.show()
