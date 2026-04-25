
import numpy as np
from scipy.special import gamma

def dirichlet_pdf(alpha, x):
    """
    Calculate the PDF of the Dirichlet distribution.

    Parameters:
    alpha: array-like, shape (k,)
        The concentration parameters of the Dirichlet distribution.
    x: array-like, shape (k,)
        The input points where the PDF is evaluated. Must sum to 1.

    Returns:
    float
        The value of the PDF at x.
    """
    if np.sum(x) != 1:
        raise ValueError("Input x must sum to 1.")
    if any(x < 0):
        raise ValueError("Input x must be non-negative.")

    k = len(alpha)
    numerator = np.prod(x ** (alpha - 1))
    denominator = np.prod(gamma(alpha)) / gamma(np.sum(alpha))

    return numerator / denominator

# Example usage
alpha = [2, 3, 5]  # Concentration parameters
x = [0.1, 0.2, 0.7]  # Points where PDF is evaluated; should sum to 1

pdf_value = dirichlet_pdf(alpha, x)
print(f"PDF value: {pdf_value}")
