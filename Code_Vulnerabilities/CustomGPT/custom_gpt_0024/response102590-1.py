
import numpy as np
from scipy.stats import dirichlet

# Define the parameters of the Dirichlet distribution (alpha parameters)
alpha = [1.0, 2.0, 3.0]  # Example alpha parameters
x = [0.2, 0.5, 0.3]      # A point in the simplex where you want to evaluate the pdf

# Calculate the pdf
pdf_value = dirichlet.pdf(x, alpha)
print(f"The pdf value at {x} for the Dirichlet distribution with alpha {alpha} is: {pdf_value}")
