
import numpy as np
from scipy.special import gammaln

def dirichlet_pdf(alpha, x):
    """
    Calculate the PDF of the Dirichlet distribution.

    Parameters:
    alpha: array-like, shape (K,)
        Concentration parameters of the Dirichlet distribution.
    x: array-like, shape (K,)
        The probability vector to evaluate (must sum to 1).

    Returns:
    float
        The PDF of the Dirichlet distribution at point x.
    """
    if not np.isclose(np.sum(x), 1):
        raise ValueError("The input vector x must sum to 1.")

    K = len(alpha)
    return (np.prod(x ** (alpha - 1)) * np.exp(-np.sum(gammaln(alpha)))) / gammaln(np.sum(alpha))

# Example usage
alpha = np.array([2.0, 3.0, 5.0])  # Concentration parameters
x = np.array([0.1, 0.5, 0.4])       # A valid probability vector

pdf_value = dirichlet_pdf(alpha, x)
print("PDF value:", pdf_value)
