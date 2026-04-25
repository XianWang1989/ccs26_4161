
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

# Sample data
np.random.seed(0)
num_lines = 10
x = np.linspace(0, 10, 100)

# Generate random 'y' data that correspond to distinct solutions (lines)
data = [np.sin(x) + np.random.normal(0, 0.1, size=x.shape) + i for i in range(num_lines)]

# Generate random probabilities for each line (for alpha blending)
probs = np.random.rand(num_lines)

# Normalize probabilities to range [0, 1]
norm_probs = (probs - probs.min()) / (probs.max() - probs.min())

# Create a 2D plot
plt.figure(figsize=(10, 6))

# Loop through each line and plot it
for i in range(num_lines):
    # Use a colormap to set colors based on probability
    color = cm.viridis(norm_probs[i])  # Using Viridis colormap
    plt.plot(x, data[i], color=color, alpha=norm_probs[i], label=f'Solution {i+1}')

plt.title('Density Plot with Distinct Lines')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.grid()
plt.show()
