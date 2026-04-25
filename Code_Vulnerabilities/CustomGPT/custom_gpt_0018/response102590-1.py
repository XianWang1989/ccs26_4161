
import numpy as np
from scipy.stats import dirichlet

# Parameters of the Dirichlet distribution (alpha parameters)
alpha = [0.5, 1.0, 1.5]

# Sample point (must be a valid point in the simplex)
x = np.array([0.2, 0.3, 0.5])

# Calculate the PDF
pdf_value = dirichlet.pdf(x, alpha)

print(f"PDF value at {x} for Dirichlet distribution with alpha {alpha}: {pdf_value}")
