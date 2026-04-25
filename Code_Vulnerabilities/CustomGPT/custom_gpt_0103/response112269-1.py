
import numpy as np
import matplotlib.pyplot as plt

# Sample data: two distinct lines with associated probabilities
x1 = np.linspace(-2, 2, 100)
y1 = 0.5 * x1**2  # Quadratic
prob1 = 0.7  # Probability for line 1

x2 = np.linspace(-2, 2, 100)
y2 = -0.5 * (x2**2 - 1)  # Inverted quadratic
prob2 = 0.3  # Probability for line 2

# Create the plot
plt.figure(figsize=(10, 8))

# Plotting the first line
plt.plot(x1, y1, color='blue', alpha=prob1, linewidth=2, label='Solution 1 (Prob: 0.7)')
# Plotting the second line
plt.plot(x2, y2, color='red', alpha=prob2, linewidth=2, label='Solution 2 (Prob: 0.3)')

# Aesthetics
plt.xlim([-2, 2])
plt.ylim([-2, 2])
plt.title('2D Density Plot with Distinct Lines')
plt.xlabel('Parameter X')
plt.ylabel('Parameter Y')
plt.axhline(0, color='black',linewidth=0.5, ls='--')
plt.axvline(0, color='black',linewidth=0.5, ls='--')
plt.grid()
plt.legend()

plt.show()
