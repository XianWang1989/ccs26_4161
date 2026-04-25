
import numpy as np
from scipy.stats import dirichlet

# Parameters for the Dirichlet distribution
alpha = np.array([2.0, 5.0, 3.0])  # Example concentration parameters

# Sample points (must sum to 1)
x = np.array([0.2, 0.5, 0.3])  # Example point in the simplex

# Calculate the pdf
pdf_value = dirichlet.pdf(x, alpha)

print(f"The pdf value at {x} is {pdf_value}")
