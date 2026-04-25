
import numpy as np
from scipy.special import gamma

def dirichlet_pdf(alpha, x):
    """
    Calculate the PDF of the Dirichlet distribution.

    Parameters:
    alpha : array-like
        Concentration parameters of the Dirichlet distribution.
    x : array-like
        The point at which to evaluate the PDF (must sum to 1).

    Returns:
    float
        The PDF value.
    """
    if not np.isclose(np.sum(x), 1):
        raise ValueError("The sum of x must be 1.")
    if any(val < 0 for val in x):
        raise ValueError("All values in x must be non-negative.")

    # Compute the PDF
    K = len(alpha)
    numerator = np.prod(x ** (alpha - 1))
    denominator = gamma(np.sum(alpha)) / np.prod(gamma(alpha))

    return numerator / denominator

# Example usage
alpha = [2, 3, 5]
x = [0.1, 0.2, 0.7]  # x should sum to 1
pdf_value = dirichlet_pdf(alpha, x)
print("PDF value:", pdf_value)
