
import numpy as np
from scipy.special import gamma

def dirichlet_pdf(x, alpha):
    """
    Compute the PDF of the Dirichlet distribution.

    Parameters:
    x: array-like, shape (K,) - probabilities where sum(x) = 1
    alpha: array-like, shape (K,) - concentration parameters

    Returns:
    pdf: float - the value of the PDF
    """
    if np.sum(x) != 1:
        raise ValueError("The sum of x must be 1.")
    if np.any(x < 0):
        raise ValueError("All elements of x must be non-negative.")

    K = len(alpha)
    numerator = np.prod(x ** (alpha - 1))
    denominator = gamma(np.sum(alpha)) / np.prod(gamma(alpha))

    return numerator / denominator

# Example usage
alpha = [1, 2, 3]
x = [0.2, 0.5, 0.3]
pdf_value = dirichlet_pdf(x, alpha)
print(f"PDF value: {pdf_value}")
