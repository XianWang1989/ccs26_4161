
import numpy as np
from scipy.special import gammaln

def dirichlet_pdf(alpha, x):
    """
    Calculate the pdf of the Dirichlet distribution.

    :param alpha: array-like, shape (K,)
        The concentration parameters of the Dirichlet distribution.
    :param x: array-like, shape (K,)
        The input points where the pdf is evaluated. Must be a valid probability vector (sum of elements = 1).
    :return: float
        The pdf value at x.
    """
    # Check if x is a valid probability vector
    if not np.all(np.isclose(np.sum(x), 1)) or np.any(x < 0):
        raise ValueError("Input x must be a valid probability vector (non-negative and sum equals 1).")

    K = len(alpha)
    return np.exp(np.sum((alpha - 1) * np.log(x)) - np.sum(gammaln(alpha)) + gammaln(np.sum(alpha)))

# Example usage
alpha = np.array([2.0, 3.0, 5.0])  # Dirichlet parameters
x = np.array([0.1, 0.2, 0.7])      # Probability vector

pdf_value = dirichlet_pdf(alpha, x)
print("PDF value:", pdf_value)
