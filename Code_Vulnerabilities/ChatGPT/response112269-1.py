
import numpy as np
import matplotlib.pyplot as plt

def generate_lines(num_lines, points_per_line):
    """Generate distinct lines in 2D space with probability density."""
    lines = []
    for i in range(num_lines):
        x = np.linspace(0, 10, points_per_line)
        # Create a line with some slope (randomly chosen)
        slope = np.random.uniform(0.1, 2)
        y = slope * x + np.random.uniform(-1, 1)  # Add some y-offset
        lines.append((x, y, slope))
    return lines

def plot_density_lines(lines, alpha_max=0.8, n_points=100):
    """Plot the distinct lines with blending."""
    plt.figure(figsize=(8, 6))

    # Create a scatter to accumulate the densities
    x_combined = np.array([])
    y_combined = np.array([])

    for x, y, slope in lines:
        # Create a density effect by plotting lines
        plt.plot(x, y, color='blue', alpha=alpha_max, linewidth=2)

        # Sum the contributions for density estimation
        x_combined = np.concatenate((x_combined, x))
        y_combined = np.concatenate((y_combined, y))

    # Optionally, use a histogram to visualize density
    plt.hist2d(x_combined, y_combined, bins=[30, 30], density=True, cmap='Blues', alpha=0.5)

    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('2D Density Plot of Distinct Solutions')
    plt.xlim(0, 10)
    plt.ylim(-5, 25)
    plt.colorbar(label='Density')
    plt.grid()
    plt.show()

# Generate sample lines
num_lines = 10
points_per_line = 50
lines = generate_lines(num_lines, points_per_line)

# Plot the density of the lines
plot_density_lines(lines)
