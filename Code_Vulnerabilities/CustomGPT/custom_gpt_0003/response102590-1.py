
import numpy as np
from scipy.stats import dirichlet

# Parameters for the Dirichlet distribution
alpha = [2.0, 5.0, 3.0]  # Concentration parameters

# Compute the pdf for a given point in the simplex
x = [0.1, 0.3, 0.6]  # A sample point in the probability simplex (x1 + x2 + x3 = 1)

# Calculate the pdf
pdf_value = dirichlet.pdf(x, alpha)

# Output the result
print("The pdf of the Dirichlet distribution at point", x, "is:", pdf_value)
