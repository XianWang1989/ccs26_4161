
import numpy as np
from scipy.stats import dirichlet

# Parameters for the Dirichlet distribution
alpha = [1.0, 2.0, 3.0]  # shape parameters
x = [0.2, 0.3, 0.5]       # point where we want the PDF

# Calculate the PDF
pdf_value = dirichlet.pdf(x, alpha)

print(f"The PDF value at {x} for the Dirichlet distribution with alpha={alpha} is: {pdf_value}")
