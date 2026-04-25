
import numpy as np
from scipy.special import gamma

def dirichlet_pdf(x, alpha):
    """
    Calculate the PDF of the Dirichlet distribution.

    Parameters:
    x : array_like
        A point in the simplex (must sum to 1 and be non-negative).
    alpha : array_like
        Concentration parameters (should be positive).

    Returns:
    float
        The PDF of the Dirichlet distribution at point x.
    """
    if np.any(x < 0) or not np.isclose(np.sum(x), 1):
        raise ValueError("x must be non-negative and sum to 1.")
    if np.any(alpha <= 0):
        raise ValueError("All alpha parameters must be positive.")

    numerator = np.prod(np.power(x, alpha - 1))
    denominator = np.prod(gamma(alpha)) / gamma(np.sum(alpha))

    return numerator / denominator

# Example usage
alpha = np.array([2, 3, 5])
x = np.array([0.2, 0.5, 0.3])  # Must sum to 1
pdf_value = dirichlet_pdf(x, alpha)
print(f"The PDF of the Dirichlet distribution at x is: {pdf_value}")
