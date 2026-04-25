
import numpy as np
from scipy.stats import dirichlet

# Parameters for the Dirichlet distribution
alpha = [1.0, 2.0, 3.0]  # Example concentration parameters

# Create a Dirichlet distribution object
dist = dirichlet(alpha)

# Generate a random point in the simplex (must sum to 1)
x = np.array([0.2, 0.3, 0.5])  # Example probabilities

# Calculate the pdf at point x
pdf_value = dist.pdf(x)

print(f"PDF at {x}: {pdf_value}")
