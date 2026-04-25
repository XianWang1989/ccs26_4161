
import numpy as np
from scipy.stats import dirichlet

# Parameters for the Dirichlet distribution
alpha = [1, 2, 3]  # Concentration parameters
x = np.array([0.2, 0.3, 0.5])  # Points at which to evaluate the PDF

# Calculate the PDF
pdf_value = dirichlet.pdf(x, alpha)

print("PDF value:", pdf_value)
