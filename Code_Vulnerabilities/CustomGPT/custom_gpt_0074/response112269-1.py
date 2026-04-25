
import numpy as np
import matplotlib.pyplot as plt

# Generate some sample data (replace this with your actual data)
x = np.linspace(-5, 5, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Create a figure
plt.figure(figsize=(10, 6))

# Plot with increasing alpha to give a "density" effect
for i in range(10):
    plt.plot(x, y1 + i, alpha=(i+1)/10, color='blue')  # Distinct solution 1
    plt.plot(x, y2 + i, alpha=(i+1)/10, color='red')   # Distinct solution 2

# Customize the plot
plt.title('Density Plot with Distinct Lines')
plt.xlabel('Parameter X')
plt.ylabel('Parameter Y')
plt.grid(True)
plt.show()
