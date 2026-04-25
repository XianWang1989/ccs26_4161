
import numpy as np
from scipy.special import gamma

def dirichlet_pdf(x, alpha):
    """
    Calculate the PDF of the Dirichlet distribution.

    Parameters:
    x : array_like, shape (k,)
        Point at which to evaluate the pdf. Should contain k proportions summing to 1.
    alpha : array_like, shape (k,)
        Parameters of the Dirichlet distribution.

    Returns:
    float
        The value of the pdf at x.
    """
    if np.sum(x) != 1 or np.any(x < 0):
        raise ValueError("x must be a valid probability vector (sum to 1 and non-negative)")

    k = len(alpha)
    return (gamma(np.sum(alpha)) / 
            np.prod(gamma(alpha))) * np.prod(x ** (alpha - 1))


# Example usage:
alpha = np.array([2, 5, 3])  # Parameters for the Dirichlet distribution
x = np.array([0.2, 0.5, 0.3])  # Proportions (should sum to 1)

pdf_value = dirichlet_pdf(x, alpha)
print("The pdf value is:", pdf_value)
