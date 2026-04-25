
import numpy as np
import matplotlib.pyplot as plt

# Sample data: distinct solutions forming lines
x = np.linspace(0, 10, 100)
probabilities = [0.5, 0.8, 0.3]  # Example probabilities for different lines

# Create a figure and axis
fig, ax = plt.subplots()

# Plot each line with varying opacity
for prob in probabilities:
    y = np.sin(x) + np.random.normal(scale=0.1, size=x.shape)  # Example line
    ax.plot(x, y, alpha=prob)  # Set alpha based on probability

# Set axis labels and title
ax.set_xlabel('Parameter 1')
ax.set_ylabel('Parameter 2')
ax.set_title('Density Plot with Distinct Lines')

# Show plot
plt.show()
