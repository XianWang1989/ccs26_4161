from scipy.stats import dirichlet
import numpy as np

# Define the concentration parameters (alpha)
alpha = [2, 3, 4]

# Define a point within the simplex (sums to 1)
x = [0.2, 0.3, 0.5]

# Calculate the PDF at point x
pdf_value = dirichlet.pdf(x, alpha)

print(f"The PDF of the Dirichlet distribution at {x} is: {pdf_value}")
