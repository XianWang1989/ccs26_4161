
import numpy as np
from scipy.stats import dirichlet

# Define the alpha parameters for the Dirichlet distribution
alpha = np.array([1.0, 1.0, 1.0])  # Example parameters

# Define a point at which to evaluate the pdf
x = np.array([0.2, 0.3, 0.5])  # Must sum to 1

# Calculate the pdf
pdf_value = dirichlet.pdf(x, alpha)

print(f"The PDF of the Dirichlet distribution at {x} is {pdf_value}")
