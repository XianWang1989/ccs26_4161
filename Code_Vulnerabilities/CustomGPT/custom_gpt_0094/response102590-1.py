
import numpy as np
from scipy.special import gamma

def dirichlet_pdf(x, alpha):
    """
    Calculate the PDF of the Dirichlet distribution.

    Parameters:
    x : array_like
        An array of probabilities (must sum to 1).
    alpha : array_like
        Concentration parameters (must be greater than 0).

    Returns:
    float
        The value of the PDF at point x.
    """
    if np.sum(x) != 1:
        raise ValueError("Input probabilities must sum to 1.")
    if np.any(alpha <= 0):
        raise ValueError("Concentration parameters must be greater than 0.")

    numerator = np.prod(x ** (alpha - 1))
    denominator = np.prod(gamma(alpha)) / gamma(np.sum(alpha))

    return numerator / denominator

# Example usage
alpha = np.array([2.0, 3.0, 5.0])
x = np.array([0.1, 0.3, 0.6])  # Should sum to 1
pdf_value = dirichlet_pdf(x, alpha)
print(f"The PDF value is: {pdf_value}")
