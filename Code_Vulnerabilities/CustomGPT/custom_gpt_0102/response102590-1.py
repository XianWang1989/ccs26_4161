
import numpy as np
from scipy.stats import dirichlet

# Parameters of the Dirichlet distribution
alpha = [1.0, 2.0, 3.0]  # Concentration parameters

# Points at which to evaluate the PDF
x = [0.2, 0.3, 0.5]

# Calculate the PDF
pdf_value = dirichlet.pdf(x, alpha)

print("PDF value:", pdf_value)
