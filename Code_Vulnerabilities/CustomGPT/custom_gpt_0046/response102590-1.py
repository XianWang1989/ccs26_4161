
import numpy as np
from scipy.special import gammaln

def dirichlet_pdf(alpha, x):
    """
    Calculate the PDF of the Dirichlet distribution.

    Parameters:
    alpha : array-like, shape (K,)
        The concentration parameters of the Dirichlet distribution.
    x : array-like, shape (K,)
        The point at which to evaluate the PDF (must sum to 1 and be non-negative).

    Returns:
    float
        The value of the PDF at x.
    """
    if np.any(x < 0) or not np.isclose(np.sum(x), 1):
        raise ValueError("x must be non-negative and sum to 1.")

    K = len(alpha)
    return (np.prod(x ** (alpha - 1)) / np.exp(np.sum(gammaln(alpha)))) * \
           np.exp(gammaln(np.sum(alpha)))

# Example usage
alpha = np.array([2, 3, 5])  # Concentration parameters
x = np.array([0.1, 0.5, 0.4])  # Points (must sum to 1)
pdf_value = dirichlet_pdf(alpha, x)
print("PDF value:", pdf_value)
