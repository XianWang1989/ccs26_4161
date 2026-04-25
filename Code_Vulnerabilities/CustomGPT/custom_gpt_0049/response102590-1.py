
import numpy as np
from scipy.stats import dirichlet

# Parameters (alpha) for the Dirichlet distribution
alpha = [1.0, 2.0, 3.0]  # Example concentration parameters

# Point at which to evaluate the pdf
x = [0.2, 0.3, 0.5]  # must sum to 1

# Calculate the pdf
pdf_value = dirichlet.pdf(x, alpha)

print(f"The pdf value of the Dirichlet distribution at {x} is: {pdf_value}")
