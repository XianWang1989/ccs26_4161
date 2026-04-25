
import numpy as np
from scipy.stats import dirichlet

# Parameters of the Dirichlet distribution
alpha = [1, 2, 3]  # Concentration parameters
x = [0.2, 0.5, 0.3]  # Point at which to evaluate the pdf

# Calculate the pdf
pdf_value = dirichlet.pdf(x, alpha)

print("The pdf of the Dirichlet distribution at the point", x, "is:", pdf_value)
