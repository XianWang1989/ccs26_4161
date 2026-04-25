
import numpy as np
import scipy.stats as stats

# Define the parameters for the Dirichlet distribution (α)
alpha = np.array([0.5, 0.5, 0.5])  # You can change these values as needed

# Create a Dirichlet distribution
dirichlet_dist = stats.dirichlet(alpha)

# Define a point to evaluate the PDF
x = np.array([0.2, 0.3, 0.5])  # must sum to 1

# Calculate the PDF
pdf_value = dirichlet_dist.pdf(x)

print(f"The PDF value for the Dirichlet distribution at {x} is {pdf_value}")
