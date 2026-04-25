
import numpy as np
from scipy.stats import dirichlet

# Parameters for the Dirichlet distribution
alpha = [1.0, 2.0, 3.0]  # Shape parameters
x = [0.2, 0.5, 0.3]       # Point at which to evaluate the pdf

# Calculate the pdf
pdf_value = dirichlet.pdf(x, alpha)

print(f"The pdf of the Dirichlet distribution at {x} with alpha {alpha} is: {pdf_value}")
