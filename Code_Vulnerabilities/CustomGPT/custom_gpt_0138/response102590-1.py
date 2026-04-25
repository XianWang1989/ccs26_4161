
import numpy as np
from scipy.stats import dirichlet

# Define the parameters of the Dirichlet distribution
alpha = np.array([1.0, 1.0, 1.0])  # Example alpha parameters

# Point at which to calculate the pdf
x = np.array([0.2, 0.5, 0.3])

# Calculate the pdf
pdf_value = dirichlet.pdf(x, alpha)

print(f"PDF value at {x} is: {pdf_value}")
