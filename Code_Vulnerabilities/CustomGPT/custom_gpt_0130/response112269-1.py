
import numpy as np
import matplotlib.pyplot as plt

# Generate example data
num_lines = 100
x = np.linspace(-5, 5, 100)
y_lines = [np.sin(x + np.random.uniform(0, 2 * np.pi)) + np.random.normal(scale=0.1) for _ in range(num_lines)]

# Define a function to plot the lines with varying opacities
def plot_density_lines(x, y_lines):
    plt.figure(figsize=(10, 6))

    for y in y_lines:
        plt.plot(x, y, color='blue', alpha=0.2)  # Opacity can be adjusted based on probability

    plt.title('2D Density Plot with Distinct Lines')
    plt.xlabel('Parameter 1')
    plt.ylabel('Parameter 2')
    plt.grid(True)
    plt.xlim([-5, 5])
    plt.ylim([-3, 3])
    plt.show()

# Call the function to plot
plot_density_lines(x, y_lines)
