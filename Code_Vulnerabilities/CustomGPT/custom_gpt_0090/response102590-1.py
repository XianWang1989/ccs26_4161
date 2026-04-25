
import numpy as np
from scipy.special import gammaln

def dirichlet_pdf(alpha, x):
    """
    Calculate the pdf of the Dirichlet distribution.

    Parameters:
    alpha : array-like
        The concentration parameters (must be positive).
    x : array-like
        The probability vector (must sum to 1).

    Returns:
    pdf : float
        The value of the pdf at x.
    """
    # Check that x sums to 1 and all elements are between 0 and 1
    if not np.isclose(np.sum(x), 1) or np.any(x < 0):
        raise ValueError("x must be a probability vector that sums to 1 and has no negative elements.")

    # Calculate the pdf
    k = len(alpha)
    numerator = np.prod(x ** (alpha - 1))
    denominator = np.exp(gammaln(np.sum(alpha)) - np.sum(gammaln(alpha)))

    return numerator / denominator

# Example usage
alpha = [2, 3, 5]  # concentration parameters
x = [0.1, 0.2, 0.7]  # probability vector

pdf_value = dirichlet_pdf(alpha, x)
print("Dirichlet pdf value:", pdf_value)
