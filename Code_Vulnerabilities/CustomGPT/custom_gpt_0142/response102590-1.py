
import numpy as np
from scipy.stats import dirichlet

# Parameters for the Dirichlet distribution
alpha = np.array([1.0, 2.0, 3.0])  # Concentration parameters

# Point at which to evaluate the PDF
x = np.array([0.2, 0.3, 0.5])  # This point should sum to 1 and all x[i] >= 0

# Calculate the PDF
pdf_value = dirichlet.pdf(x, alpha)

print(f"The PDF of the Dirichlet distribution at {x} is {pdf_value}")
