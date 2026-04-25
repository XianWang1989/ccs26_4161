
import numpy as np
from scipy.special import gamma

def dirichlet_pdf(x, alpha):
    """
    Calculate the pdf of the Dirichlet distribution.

    Parameters:
    x : array-like
        Points at which to evaluate the pdf (must sum to 1).
    alpha : array-like
        Concentration parameters of the Dirichlet distribution.

    Returns:
    pdf_value : float
        The value of the pdf at `x`.
    """
    if not np.isclose(np.sum(x), 1):
        raise ValueError("The elements of x must sum to 1.")

    numerator = np.prod(gamma(alpha)) * np.prod(x**(alpha - 1))
    denominator = gamma(np.sum(alpha))

    return numerator / denominator

# Example usage
alpha = [2, 3, 5]  # Concentration parameters
x = [0.1, 0.3, 0.6]  # Points (must sum to 1)

pdf_value = dirichlet_pdf(x, alpha)
print("PDF value:", pdf_value)
