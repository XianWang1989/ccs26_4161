
import numpy as np
from scipy.stats import dirichlet

# Parameters for the Dirichlet distribution
alpha = [1, 2, 3]  # concentration parameters

# Point at which to evaluate the pdf
x = [0.1, 0.3, 0.6]

# Calculate the pdf using the dirichlet class
pdf_value = dirichlet.pdf(x, alpha)

print("PDF value:", pdf_value)
