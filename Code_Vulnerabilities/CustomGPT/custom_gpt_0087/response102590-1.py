
import numpy as np
from scipy.stats import dirichlet

# Define parameters for the Dirichlet distribution
alpha = [1.0, 2.0, 3.0]  # concentration parameters

# Calculate the PDF for a specific point in the simplex
point = [0.3, 0.4, 0.3]  # must sum to 1
pdf_value = dirichlet.pdf(point, alpha)

print(f'The PDF of the Dirichlet distribution at {point} is {pdf_value}')
