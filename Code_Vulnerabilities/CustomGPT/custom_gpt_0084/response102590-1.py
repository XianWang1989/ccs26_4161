
import numpy as np
from scipy.special import gamma

def dirichlet_pdf(alpha, x):
    """
    Calculate the PDF of the Dirichlet distribution.

    Parameters:
    alpha : array-like
        The concentration parameters of the Dirichlet distribution.
    x : array-like
        The point(s) at which to evaluate the PDF. Must satisfy sum(x) = 1 and x >= 0.

    Returns:
    pdf : float
        The PDF value at x.
    """
    if not np.isclose(np.sum(x), 1):
        raise ValueError("The elements of x must sum to 1.")
    if np.any(x < 0):
        raise ValueError("All elements of x must be non-negative.")

    alpha_sum = np.sum(alpha)
    numerator = np.prod(x ** (alpha - 1))
    denominator = (gamma(alpha_sum) / 
                   np.prod(gamma(alpha)))

    return numerator / denominator

# Example usage
alpha = [2, 5, 3]  # concentration parameters
x = [0.2, 0.5, 0.3]  # point to evaluate PDF
pdf_value = dirichlet_pdf(alpha, x)
print(f"PDF value: {pdf_value}")
