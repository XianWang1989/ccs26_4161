
import numpy as np
from scipy.stats import dirichlet

# Parameters for the Dirichlet distribution
alpha = [2.0, 5.0, 3.0]  # Example concentration parameters
data_point = [0.2, 0.5, 0.3]  # Point for which to calculate the pdf

# Calculate the pdf
pdf_value = dirichlet.pdf(data_point, alpha)

print(f"The PDF of the Dirichlet distribution at {data_point} is {pdf_value:.4f}")
