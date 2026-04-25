
import numpy as np
from scipy.special import gamma

def dirichlet_pdf(x, alpha):
    """
    Calculate the PDF of the Dirichlet distribution.

    Parameters:
        x (array-like): Input vector (must sum to 1).
        alpha (array-like): Concentration parameters.

    Returns:
        float: The PDF value at x.
    """
    if not np.isclose(np.sum(x), 1):
        raise ValueError("Input vector x must sum to 1.")

    k = len(alpha)
    numerator = np.prod(x ** (alpha - 1))
    denominator = gamma(np.sum(alpha)) / np.prod(gamma(alpha))

    return numerator / denominator

# Example usage
alpha = [2.0, 5.0, 3.0]  # Concentration parameters
x = [0.1, 0.7, 0.2]  # Point at which to evaluate the PDF (must sum to 1)

pdf_value = dirichlet_pdf(x, alpha)
print(f"PDF value: {pdf_value}")
