
import numpy as np
from scipy.stats import dirichlet

# Parameters for the Dirichlet distribution
alpha = np.array([1.0, 2.0, 3.0])  # The concentration parameters

# Point at which to evaluate the pdf
x = np.array([0.2, 0.3, 0.5])  # Must be a valid Dirichlet sample (sums to 1)

# Calculate the pdf
pdf_value = dirichlet.pdf(x, alpha)

print(f"The probability density function value at {x} is: {pdf_value}")
