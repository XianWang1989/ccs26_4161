
import numpy as np
from scipy.stats import dirichlet

# Parameters of the Dirichlet distribution
alpha = np.array([1, 1, 1])  # Concentration parameters
# Sample point where you want to evaluate the PDF
x = np.array([0.2, 0.3, 0.5])  # Should sum to 1

# Calculate the PDF
pdf = dirichlet.pdf(x, alpha)

print(f"The PDF at point {x} is: {pdf}")
