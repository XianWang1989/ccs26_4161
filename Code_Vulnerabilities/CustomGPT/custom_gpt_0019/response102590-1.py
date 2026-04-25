
import numpy as np
from scipy.special import gamma

def dirichlet_pdf(alpha, x):
    """
    Calculate the PDF of the Dirichlet distribution.

    Parameters:
    alpha (array-like): The concentration parameters of the Dirichlet distribution.
    x (array-like): The points at which to evaluate the PDF (should sum to 1).

    Returns:
    float: The value of the PDF at point x.
    """
    if not np.isclose(np.sum(x), 1):
        raise ValueError("Input x must sum to 1.")
    if any(x < 0):
        raise ValueError("Input x must be non-negative.")

    # Compute the PDF
    numerator = np.prod(x ** (alpha - 1))
    denominator = np.prod(gamma(alpha)) / gamma(np.sum(alpha))

    return numerator / denominator

# Example usage
alpha = [2, 5, 3]  # Concentration parameters
x = [0.2, 0.5, 0.3]  # Point where PDF is evaluated

pdf_value = dirichlet_pdf(alpha, x)
print(f"PDF value: {pdf_value}")
