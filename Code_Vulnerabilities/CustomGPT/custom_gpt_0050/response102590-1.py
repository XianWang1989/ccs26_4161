
import numpy as np
from scipy.stats import dirichlet

# Parameters (alpha parameters)
alpha = [1.0, 2.0, 3.0]

# Point at which to evaluate the PDF
x = [0.2, 0.5, 0.3]  # Must sum to 1 for Dirichlet

# Calculate the PDF
pdf_value = dirichlet.pdf(x, alpha)

print(f"The PDF of the Dirichlet distribution at {x} is: {pdf_value}")
