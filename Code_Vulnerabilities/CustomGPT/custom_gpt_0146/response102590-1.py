
import numpy as np
from scipy.stats import dirichlet

# Define the parameters (alpha) of the Dirichlet distribution
alpha = np.array([2, 3, 4])

# Calculate the PDF for a specific point (x)
# For the Dirichlet distribution, x should be a point in the simplex
x = np.array([0.2, 0.5, 0.3])

# Calculate the PDF
pdf_value = dirichlet.pdf(x, alpha)

print("The PDF of the Dirichlet distribution at x =", x, "is:", pdf_value)
