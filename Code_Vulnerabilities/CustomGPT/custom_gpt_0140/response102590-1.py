
import numpy as np
from scipy.stats import dirichlet

# Define the concentration parameters (alpha)
alpha = np.array([1.0, 2.0, 3.0])

# Calculate the pdf for a specific point
x = np.array([0.2, 0.3, 0.5])  # Must sum to 1
pdf_value = dirichlet.pdf(x, alpha)

print(f"The pdf value at {x} is: {pdf_value}")
