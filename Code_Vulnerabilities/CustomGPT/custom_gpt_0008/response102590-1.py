
import numpy as np
from scipy.stats import dirichlet

# Parameters
alpha = [2.0, 5.0, 1.0]  # Concentration parameters
x = [0.2, 0.5, 0.3]      # Point at which to evaluate the PDF

# Calculate the PDF
pdf_value = dirichlet.pdf(x, alpha)

print(f"The PDF of the Dirichlet distribution at {x} is: {pdf_value}")
