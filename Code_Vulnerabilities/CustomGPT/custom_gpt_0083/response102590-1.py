
import numpy as np
from scipy.special import gamma

def dirichlet_pdf(alpha, x):
    """
    Calculate the PDF of the Dirichlet distribution.

    Parameters:
    alpha: array-like, shape (K,) - vector of concentration parameters
    x: array-like, shape (K,) - point at which to evaluate the PDF (must sum to 1)

    Returns:
    PDF value
    """
    if not np.isclose(np.sum(x), 1):
        raise ValueError("x must sum to 1.")
    if np.any(x < 0):
        return 0

    K = len(alpha)
    numerator = np.prod(x ** (alpha - 1))
    denominator = (gamma(np.sum(alpha)) /
                   np.prod(gamma(alpha)))

    return numerator / denominator

# Example usage
alpha = [2, 5, 3]  # Concentration parameters
x = [0.2, 0.5, 0.3]  # Point at which to evaluate PDF

pdf_value = dirichlet_pdf(alpha, x)
print("Dirichlet PDF value:", pdf_value)
