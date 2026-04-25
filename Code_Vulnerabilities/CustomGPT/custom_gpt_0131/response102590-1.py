
import numpy as np
from scipy.stats import dirichlet

# Parameters for the Dirichlet distribution
alpha = [1.0, 1.0, 1.0]  # The concentration parameters
sample = [0.2, 0.5, 0.3]  # A sample from the simplex

# Calculate the probability density function (pdf)
pdf_value = dirichlet.pdf(sample, alpha)

print("PDF value:", pdf_value)
