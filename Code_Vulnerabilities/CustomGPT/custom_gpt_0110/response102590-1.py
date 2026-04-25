
import numpy as np
from scipy.stats import dirichlet

# Define the alpha parameters for the Dirichlet distribution
alpha = np.array([1.0, 2.0, 3.0])

# Sample points in the simplex (must sum to 1)
x = np.array([0.2, 0.5, 0.3])  # This is a valid point in the simplex

# Calculate the PDF at the point x
pdf_value = dirichlet.pdf(x, alpha)

print(f"PDF of Dirichlet distribution at {x} with alpha {alpha}: {pdf_value}")
