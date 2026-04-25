
import numpy as np
from scipy.special import gamma

def dirichlet_pdf(alpha, x):
    """
    Calculate the PDF of a Dirichlet distribution.

    Parameters:
    alpha : array-like, shape (K,)
        The parameter of the Dirichlet distribution.
    x : array-like, shape (K,)
        The point at which to evaluate the PDF (must sum to 1).

    Returns:
    float
        The value of the PDF at x.
    """
    # Check if x is a valid point (sums to 1 and non-negative)
    if not np.isclose(np.sum(x), 1) or np.any(x < 0):
        raise ValueError("x must be a non-negative array that sums to 1")

    K = len(alpha)
    numerator = np.prod(x**(alpha - 1))
    denominator = gamma(np.sum(alpha)) / np.prod(gamma(alpha))

    return numerator / denominator

# Example parameters
alpha = np.array([2.0, 1.0, 1.0])  # Parameters of the Dirichlet
x = np.array([0.5, 0.3, 0.2])  # Point at which to evaluate the PDF

pdf_value = dirichlet_pdf(alpha, x)
print(f"The PDF of the Dirichlet distribution at {x} is {pdf_value}")
