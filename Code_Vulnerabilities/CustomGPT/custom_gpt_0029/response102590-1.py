
import numpy as np
from scipy.stats import dirichlet

# Define the alpha parameters for the Dirichlet distribution
alpha = [1.0, 2.0, 3.0]

# Create a Dirichlet distribution instance
dist = dirichlet(alpha)

# Define a point to evaluate the pdf
point = [0.2, 0.3, 0.5]

# Calculate the pdf at the specified point
pdf_value = dist.pdf(point)

print(f"The pdf value at {point} is {pdf_value}")
