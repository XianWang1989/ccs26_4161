
import numpy as np
from scipy.special import gamma

def dirichlet_pdf(x, alpha):
    """
    Calculate the PDF of the Dirichlet distribution.

    Parameters:
    x : array-like, shape (K,)
        The input for which to compute the PDF. Must sum to 1.
    alpha : array-like, shape (K,)
        The concentration parameters of the Dirichlet distribution.

    Returns:
    float
        The value of the PDF at x.
    """
    if not np.isclose(np.sum(x), 1):
        raise ValueError("Input x must sum to 1.")

    K = len(alpha)
    numerator = np.prod(x**(alpha - 1))
    denominator = gamma(np.sum(alpha)) / np.prod(gamma(alpha))

    return numerator / denominator

# Example usage
alpha = [1, 2, 3]  # Concentration parameters
x = [0.2, 0.5, 0.3]  # Input should sum to 1

pdf_value = dirichlet_pdf(x, alpha)
print("PDF value:", pdf_value)
