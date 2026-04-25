
import numpy as np
from scipy.stats import dirichlet

# Parameters for the Dirichlet distribution
alpha = [1.0, 2.0, 3.0]  # Concentration parameters

# Point at which to calculate the pdf
x = [0.2, 0.3, 0.5]

# Calculate the pdf
pdf_value = dirichlet.pdf(x, alpha)

print(f"The pdf of the Dirichlet distribution at {x} is {pdf_value}")
