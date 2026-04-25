
import numpy as np
from scipy.stats import dirichlet

# Parameters for the Dirichlet distribution
alpha = [1.0, 2.0, 3.0]  # example alpha parameters
x = [0.2, 0.3, 0.5]  # example point where you want to compute the pdf

# Calculate the pdf
pdf_value = dirichlet.pdf(x, alpha)

print(f"The pdf value at {x} is: {pdf_value}")
