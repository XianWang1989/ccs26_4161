
import numpy as np
from scipy.stats import dirichlet

# Parameters of the Dirichlet distribution
alpha = [1.0, 2.0, 3.0]

# Sample point where you want to evaluate the PDF
x = [0.1, 0.5, 0.4]

# Ensure x is a valid point in the simplex (i.e., sums to 1)
if np.isclose(sum(x), 1) and all(i >= 0 for i in x):
    pdf_value = dirichlet.pdf(x, alpha)
    print(f"PDF value at {x} for Dirichlet distribution with alpha {alpha}: {pdf_value}")
else:
    print("The sample point must be in the simplex (non-negative and sums to 1).")
