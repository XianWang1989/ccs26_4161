
import numpy as np
from scipy.special import gamma

def dirichlet_pdf(x, alpha):
    """
    Calculate the PDF of the Dirichlet distribution for a given alpha and x.

    Parameters:
    x : array-like, shape (k,)
        Sample points (must sum to 1).
    alpha : array-like, shape (k,)
        Concentration parameters (positive).

    Returns:
    float
        PDF value at x.
    """
    if not np.isclose(np.sum(x), 1):
        raise ValueError("Elements of x must sum to 1.")

    if any(a <= 0 for a in alpha):
        raise ValueError("All elements of alpha must be positive.")

    k = len(x)
    numerator = np.prod(x**(alpha - 1))
    denominator = gamma(np.sum(alpha)) / np.prod(gamma(alpha))

    return numerator / denominator

# Example usage
alpha = [2, 3, 5]
x = [0.1, 0.2, 0.7]  # Must sum to 1
pdf_value = dirichlet_pdf(x, alpha)
print("PDF Value:", pdf_value)
