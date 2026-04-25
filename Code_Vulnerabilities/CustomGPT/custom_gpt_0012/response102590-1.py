
import numpy as np
from scipy.stats import dirichlet

# Parameters for the Dirichlet distribution
alpha = [1.0, 1.0, 1.0]  # Concentration parameters

# Point at which to evaluate the PDF
x = [0.2, 0.3, 0.5]

# Calculate the PDF
pdf_value = dirichlet.pdf(x, alpha)

print("PDF of the Dirichlet distribution at", x, ":", pdf_value)
