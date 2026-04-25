
import numpy as np
from scipy.stats import dirichlet

# Parameters for the Dirichlet distribution
alpha = np.array([2.0, 5.0, 3.0])  # Concentration parameters

# Sample point where you want to calculate the PDF
x = np.array([0.2, 0.5, 0.3])  # Must satisfy 0 <= x_i <= 1 and sum(x) = 1

# Calculate PDF
pdf_value = dirichlet.pdf(x, alpha)

print("PDF value at x:", pdf_value)
