
import numpy as np
from scipy.stats import dirichlet

# Parameters for the Dirichlet distribution
alpha = np.array([1.0, 1.0, 1.0])  # Example alpha values for 3 components

# Define a point where you want to calculate the pdf
x = np.array([0.2, 0.3, 0.5])  # Example point in the simplex

# Calculate the pdf
pdf_value = dirichlet.pdf(x, alpha)

print(f'The pdf of the Dirichlet distribution at point {x} is: {pdf_value}')
