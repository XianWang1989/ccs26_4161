
import numpy as np
from scipy.special import gamma

def dirichlet_pdf(x, alpha):
    """
    Compute the probability density function of the Dirichlet distribution.

    Parameters:
    - x: array-like, shape (k,)
        Points at which to evaluate the pdf, must sum to 1.
    - alpha: array-like, shape (k,)
        Concentration parameters, strictly positive.

    Returns:
    - pdf: float
        The evaluated probability density function at point x.
    """
    if np.sum(x) != 1 or np.any(x < 0):
        raise ValueError("x must be a vector that sums to 1 and is non-negative.")

    if np.any(alpha <= 0):
        raise ValueError("All alpha values must be strictly positive.")

    # Calculate the normalization constant B(alpha)
    B_alpha = gamma(np.sum(alpha)) / np.prod(gamma(alpha))

    # Calculate the PDF
    pdf = (np.prod(x ** (alpha - 1))) / B_alpha

    return pdf

# Example usage:
alpha = np.array([2.0, 3.0, 5.0])  # Concentration parameters
x = np.array([0.1, 0.5, 0.4])  # This should sum to 1

pdf_value = dirichlet_pdf(x, alpha)
print("Dirichlet PDF value:", pdf_value)
