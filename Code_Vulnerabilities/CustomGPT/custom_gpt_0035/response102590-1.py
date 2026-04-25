
import numpy as np
from scipy.stats import dirichlet

# Parameters for the Dirichlet distribution
alpha = np.array([1.0, 2.0, 3.0])  # Dirichlet parameters
x = np.array([0.2, 0.3, 0.5])       # Point at which to evaluate the PDF

# Calculate the PDF
pdf_value = dirichlet.pdf(x, alpha)

print(f'The PDF value of the Dirichlet distribution at {x} is: {pdf_value}')
