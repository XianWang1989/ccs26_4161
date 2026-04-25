
import numpy as np
from scipy.special import gammaln

def dirichlet_pdf(alpha, x):
    # Validate inputs
    if not np.all(x >= 0) or not np.isclose(np.sum(x), 1):
        raise ValueError("x must be non-negative and sum to 1.")

    # Compute the pdf of the Dirichlet distribution
    numerator = np.prod(np.power(x, alpha - 1))
    denominator = np.exp(gammaln(np.sum(alpha)) - np.sum(gammaln(alpha)))

    return numerator / denominator

# Example usage
alpha = np.array([2, 3, 5])  # Parameters of the Dirichlet distribution
x = np.array([0.1, 0.3, 0.6])  # Point at which to evaluate the pdf

pdf_value = dirichlet_pdf(alpha, x)
print(f"The pdf value at x = {x} is: {pdf_value}")
