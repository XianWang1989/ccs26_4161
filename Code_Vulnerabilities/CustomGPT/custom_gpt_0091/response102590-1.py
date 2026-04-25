
import numpy as np
from scipy.stats import dirichlet

# Parameters for the Dirichlet distribution
alpha = [2.0, 5.0, 3.0]  # concentration parameters

# Prepare a sample point in the simplex (must sum to 1)
x = [0.2, 0.5, 0.3]

# Calculate the pdf at point x
pdf_value = dirichlet.pdf(x, alpha)

print(f"The pdf value of the Dirichlet distribution at point {x} is: {pdf_value}")
