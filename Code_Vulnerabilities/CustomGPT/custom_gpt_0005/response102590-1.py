
import numpy as np
from scipy.stats import dirichlet

# Parameters for the Dirichlet distribution
alpha = np.array([1.0, 2.0, 3.0])  # concentration parameters
x = np.array([0.2, 0.3, 0.5])       # point at which to evaluate the PDF

# Calculate the PDF
pdf_value = dirichlet.pdf(x, alpha)

print("PDF of the Dirichlet distribution at x:", pdf_value)
