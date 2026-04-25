
import numpy as np
from scipy.stats import dirichlet

# Parameters for the Dirichlet distribution
alpha = [1.0, 2.0, 3.0]  # shape parameters
x = [0.2, 0.5, 0.3]       # a point in the simplex

# Calculate the pdf
pdf_value = dirichlet.pdf(x, alpha)

print(f"The pdf value for x={x} is: {pdf_value}")
