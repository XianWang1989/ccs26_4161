
import numpy as np
from scipy.special import gamma

def dirichlet_pdf(x, alpha):
    """
    Calculate the pdf of the Dirichlet distribution.

    Parameters:
    x : array-like, shape (k,)
        The point at which to evaluate the pdf. All elements must be non-negative
        and sum to 1.
    alpha : array-like, shape (k,)
        The concentration parameters of the Dirichlet distribution.

    Returns:
    pdf : float
        The evaluated pdf at point x.
    """
    if np.sum(x) != 1 or np.any(x < 0):
        raise ValueError("Input x must be a probability vector (non-negative and sum to 1).")

    k = len(alpha)

    numerator = np.prod(x ** (alpha - 1))
    denominator = gamma(np.sum(alpha)) / np.prod(gamma(alpha))

    return numerator / denominator

# Example usage:
alpha = [2, 3, 5]  # concentration parameters
x = [0.1, 0.2, 0.7]  # must sum to 1

pdf_value = dirichlet_pdf(x, alpha)
print("PDF value:", pdf_value)
