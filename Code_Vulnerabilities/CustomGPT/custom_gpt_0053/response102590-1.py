
import numpy as np
from scipy.stats import dirichlet

# Parameters for the Dirichlet distribution
alpha = [2.0, 5.0, 3.0]  # shape parameters
# A point on the simplex (sum of components should be 1)
point = [0.2, 0.5, 0.3]

# Calculate the pdf
pdf_value = dirichlet.pdf(point, alpha)

print(f"The pdf value at {point} is: {pdf_value}")
