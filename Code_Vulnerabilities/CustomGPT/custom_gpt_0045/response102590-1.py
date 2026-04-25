
import numpy as np
from scipy.special import gamma

def dirichlet_pdf(x, alpha):
    """
    Calculate the pdf of the Dirichlet distribution.

    Parameters:
    x : array-like
        A vector of shape parameters (must sum to 1 and lie in the interval [0, 1]).
    alpha : array-like
        An array containing the concentration parameters (alpha > 0).

    Returns:
    float
        The pdf value of the Dirichlet distribution at x.
    """
    # Check that the sum of x is 1
    if not np.isclose(np.sum(x), 1):
        raise ValueError("The sum of x must be 1.")

    # Calculate the pdf
    numerator = np.prod(x ** (alpha - 1))
    denominator = np.prod(gamma(alpha)) / gamma(np.sum(alpha))

    return numerator / denominator

# Example usage
alpha = np.array([1.0, 2.0, 3.0])  # Concentration parameters
x = np.array([0.1, 0.2, 0.7])       # Point where we want to compute the pdf

pdf_value = dirichlet_pdf(x, alpha)
print("The pdf of the Dirichlet distribution at x is:", pdf_value)
