
import numpy as np
from scipy.stats import dirichlet

# Parameters for the Dirichlet distribution
alpha = np.array([2.0, 5.0, 3.0])  # Concentration parameters

# The point at which to evaluate the pdf
x = np.array([0.2, 0.3, 0.5])

# Calculate the pdf
pdf_value = dirichlet.pdf(x, alpha)

print(f"PDF of Dirichlet distribution at {x}: {pdf_value}")
