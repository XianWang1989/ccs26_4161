
import numpy as np
from scipy.special import gamma

def dirichlet_pdf(alpha, x):
    """
    Calculate the PDF of the Dirichlet distribution.

    Parameters:
    alpha : array_like
        The concentration parameters of the Dirichlet distribution.
    x : array_like
        The input values (should sum to 1 and be in the range [0, 1]).

    Returns:
    float
        The value of the PDF at x.
    """
    if np.any(x < 0) or np.any(x > 1) or not np.isclose(np.sum(x), 1):
        raise ValueError("x must be in the range [0, 1] and sum to 1.")

    k = len(alpha)
    numerator = np.prod(x ** (alpha - 1))
    denominator = gamma(np.sum(alpha)) / np.prod(gamma(alpha))
    return numerator / denominator

# Example usage
alpha = np.array([2, 5, 3])  # Concentration parameters
x = np.array([0.1, 0.7, 0.2])  # Values that sum to 1
pdf_value = dirichlet_pdf(alpha, x)

print("PDF of Dirichlet distribution:", pdf_value)
