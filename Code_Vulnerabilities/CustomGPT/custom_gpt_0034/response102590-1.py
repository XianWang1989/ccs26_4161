
import numpy as np
from scipy.special import gamma

def dirichlet_pdf(alpha, x):
    """Calculate the pdf of the Dirichlet distribution.

    Args:
        alpha (array-like): Concentration parameters of the Dirichlet distribution.
        x (array-like): Points at which to evaluate the pdf (should sum to 1).

    Returns:
        float: The probability density at point x.
    """
    if not np.isclose(np.sum(x), 1):
        raise ValueError("x must sum to 1.")

    numerator = np.prod(x**(alpha - 1))
    denominator = gamma(np.sum(alpha)) / np.prod(gamma(alpha))

    return numerator / denominator

# Example usage
alpha = [1, 2, 3]
x = [0.1, 0.6, 0.3]
pdf_value = dirichlet_pdf(alpha, x)
print(f"PDF value: {pdf_value}")
