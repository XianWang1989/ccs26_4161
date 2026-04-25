
import numpy as np
from scipy.stats import dirichlet

# Parameters for the Dirichlet distribution
alpha = np.array([1.0, 2.0, 3.0])  # shape parameters
x = np.array([0.1, 0.2, 0.7])       # point at which to calculate pdf

# Calculate the pdf
pdf_value = dirichlet.pdf(x, alpha)

print(f"The pdf value of the Dirichlet distribution at {x} is {pdf_value}.")
