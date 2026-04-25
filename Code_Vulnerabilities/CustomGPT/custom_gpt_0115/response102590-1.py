
import numpy as np
from scipy.special import gamma

def dirichlet_pdf(alpha, x):
    """
    Calculate the PDF of the Dirichlet distribution.

    Parameters:
    alpha (array-like): The concentration parameters (must be > 0).
    x (array-like): The point(s) at which to evaluate the PDF (must sum to 1).

    Returns:
    float: The value of the PDF at x.
    """
    if len(alpha) != len(x) or not np.allclose(np.sum(x), 1) or np.any(x < 0):
        raise ValueError("x must be the same length as alpha, sum to 1 and all elements non-negative.")

    coeff = gamma(np.sum(alpha)) / np.prod(gamma(alpha))
    return coeff * np.prod(x**(alpha - 1))

# Example usage:
alpha = [2.0, 3.0, 5.0]  # Concentration parameters
x = [0.2, 0.5, 0.3]      # A point in the simplex

pdf_value = dirichlet_pdf(alpha, x)
print("PDF value:", pdf_value)
