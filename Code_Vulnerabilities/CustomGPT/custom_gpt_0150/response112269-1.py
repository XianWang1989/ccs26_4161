
import numpy as np
import matplotlib.pyplot as plt

# Sample data: distinct solutions forming lines
num_lines = 100
x = np.linspace(0, 10, 500)

# Create an array of different probabilities for each solution
probabilities = np.random.rand(num_lines)

# Create a figure
plt.figure(figsize=(10, 6))

# Plot each line with an opacity corresponding to its probability
for i in range(num_lines):
    # Generate lines: y = mx + b where m is a random slope and b a random intercept
    m = np.random.uniform(-2, 2)
    b = np.random.uniform(0, 10)
    y = m * x + b

    # Plot the line with opacity based on corresponding probability
    plt.plot(x, y, alpha=probabilities[i], color='blue')

# Set plot limits and labels
plt.xlim(0, 10)
plt.ylim(0, 10)
plt.title('Density Plot with Distinct Lines')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid()

# Show plot
plt.show()
