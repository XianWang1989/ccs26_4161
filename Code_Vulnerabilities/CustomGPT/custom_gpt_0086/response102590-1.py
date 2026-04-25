
import numpy as np
from scipy.stats import dirichlet

# Parameters for the Dirichlet distribution
alpha = [1.0, 2.0, 3.0]  # shape parameters

# Point at which to calculate the PDF
x = [0.2, 0.3, 0.5]  # must sum to 1

# Calculate the PDF
pdf_value = dirichlet.pdf(x, alpha)

print("PDF of the Dirichlet distribution at point x:", pdf_value)
