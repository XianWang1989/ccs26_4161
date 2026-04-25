
import numpy as np
from scipy.stats import dirichlet

# Parameters for the Dirichlet distribution
alpha = [2.0, 3.0, 5.0]  # alpha parameters of the distribution

# Create the Dirichlet distribution object
d = dirichlet(alpha)

# Points where you want to evaluate the PDF
x = [0.2, 0.3, 0.5]  # should sum to 1

# Calculate the PDF at the points x
pdf_value = d.pdf(x)

print(f"The PDF value at {x} is: {pdf_value}")
