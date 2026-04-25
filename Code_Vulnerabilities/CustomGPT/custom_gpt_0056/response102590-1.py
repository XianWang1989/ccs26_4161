
import numpy as np
from scipy.stats import dirichlet

# Parameters for the Dirichlet distribution
alpha = [1.0, 2.0, 3.0]  # Concentration parameters
samples = [0.2, 0.3, 0.5]  # Sample point

# Calculate the PDF at the given sample point
pdf_value = dirichlet.pdf(samples, alpha)

print(f"The PDF of the Dirichlet distribution at {samples} is: {pdf_value}")
