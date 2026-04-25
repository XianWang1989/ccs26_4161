
import numpy as np
from scipy.special import gamma

def dirichlet_pdf(x, alpha):
    """
    Calculate the PDF of the Dirichlet distribution.

    Parameters:
    - x: Array-like, shape (K,) where K is the dimension of the distribution.
    - alpha: Array-like, shape (K,), concentration parameters.

    Returns:
    - pdf: The probability density function evaluated at x.
    """
    if np.any(x < 0) or np.sum(x) != 1:
        raise ValueError("Input must be a valid probability vector that sums to 1.")

    K = len(alpha)
    numerator = np.prod(x**(alpha - 1))
    denominator = gamma(np.sum(alpha)) / np.prod(gamma(alpha))

    return numerator / denominator

# Example usage:
alpha = [1, 1, 1]  # Concentration parameters (simple symmetric Dirichlet)
x = [0.2, 0.5, 0.3]  # A valid probability vector

pdf_value = dirichlet_pdf(x, alpha)
print("PDF value:", pdf_value)
