
import numpy as np
from scipy.special import gammaln

def dirichlet_pdf(x, alpha):
    """
    Compute the PDF of the Dirichlet distribution.

    Parameters:
    x : array-like, shape (k,)
        The point at which to evaluate the PDF (should sum to 1).
    alpha : array-like, shape (k,)
        The concentration parameters (alpha > 0).

    Returns:
    pdf : float
        The value of the PDF at point x.
    """
    if np.sum(x) != 1:
        raise ValueError("x must sum to 1")
    if np.any(alpha <= 0):
        raise ValueError("All alpha parameters must be positive")

    k = len(alpha)
    # Calculate the PDF using the formula
    numerator = np.prod(x ** (alpha - 1))
    denominator = np.exp(gammaln(np.sum(alpha)) - np.sum(gammaln(alpha)))

    return numerator / denominator

# Example usage
alpha = [2.0, 3.0, 5.0]  # Concentration parameters
x = [0.2, 0.3, 0.5]      # Point at which to evaluate PDF (must sum to 1)
pdf_value = dirichlet_pdf(x, alpha)
print("PDF value:", pdf_value)
