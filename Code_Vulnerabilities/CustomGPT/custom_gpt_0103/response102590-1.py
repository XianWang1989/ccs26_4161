
import numpy as np
from scipy.stats import dirichlet

# Parameters for the Dirichlet distribution (alpha parameters)
alpha = np.array([1, 2, 3])  # Example alpha values

# Point at which to evaluate the pdf
x = np.array([0.2, 0.3, 0.5])  # Must sum to 1

# Calculate the pdf
pdf_value = dirichlet.pdf(x, alpha)

print(f'The pdf value at {x} is: {pdf_value}')
