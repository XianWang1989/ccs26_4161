
import numpy as np
from scipy.stats import dirichlet

# Parameters for the Dirichlet distribution (alpha values)
alpha = np.array([1.0, 2.0, 3.0])

# Point at which to evaluate the PDF
x = np.array([0.2, 0.3, 0.5])

# Ensure that x sums to 1 and all elements are non-negative
if np.all(x >= 0) and np.isclose(np.sum(x), 1):
    pdf_value = dirichlet.pdf(x, alpha)
    print(f'The PDF at {x} for Dirichlet distribution with alpha {alpha} is: {pdf_value}')
else:
    print("x must be a non-negative vector that sums to 1.")
