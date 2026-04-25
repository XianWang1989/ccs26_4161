
import numpy as np
from scipy.special import gamma

def dirichlet_pdf(x, alpha):
    """
    Calculate the pdf of the Dirichlet distribution.

    Parameters:
    x : array-like
        Input probabilities (must sum to 1).
    alpha : array-like
        Concentration parameters (must be positive).

    Returns:
    float
        The probability density function value.
    """
    if not np.isclose(np.sum(x), 1):
        raise ValueError("Input probabilities must sum to 1.")

    if np.any(alpha <= 0):
        raise ValueError("Concentration parameters must be positive.")

    numerator = np.prod(x**(alpha - 1))
    denominator = np.prod(gamma(alpha)) / gamma(np.sum(alpha))

    return numerator / denominator

# Example usage
alpha = [2, 5, 3]  # concentration parameters
x = [0.2, 0.5, 0.3]  # example probabilities

pdf_value = dirichlet_pdf(x, alpha)
print(f"PDF value: {pdf_value}")
