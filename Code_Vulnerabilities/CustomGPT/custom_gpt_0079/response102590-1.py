
import numpy as np
from scipy.special import gamma

def dirichlet_pdf(alpha, x):
    """
    Calculate the pdf of the Dirichlet distribution.

    Parameters:
    alpha : array-like
        The parameters of the Dirichlet distribution (must be positive).
    x : array-like
        A point at which to evaluate the pdf (must sum to 1 and be non-negative).

    Returns:
    float
        The value of the pdf at point x.
    """
    if len(alpha) != len(x) or np.any(x < 0) or not np.isclose(np.sum(x), 1):
        raise ValueError("Invalid inputs: x must be non-negative and sum to 1.")

    numerator = np.prod(x ** (alpha - 1))
    denominator = np.prod(gamma(alpha)) / gamma(np.sum(alpha))

    return numerator / denominator

# Example usage:
alpha = [2.0, 3.0, 5.0]  # Parameters of the Dirichlet distribution
x = [0.1, 0.3, 0.6]      # Point at which to evaluate

pdf_value = dirichlet_pdf(alpha, x)
print("PDF value:", pdf_value)
