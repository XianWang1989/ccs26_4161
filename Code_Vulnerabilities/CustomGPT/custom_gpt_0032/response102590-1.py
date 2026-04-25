
import numpy as np
from scipy.special import gamma

def dirichlet_pdf(alpha, x):
    """
    Calculate the PDF of the Dirichlet distribution.

    Parameters:
    alpha : array-like
        The concentration parameters of the Dirichlet distribution.
    x : array-like
        The point(s) at which to evaluate the PDF. Should be a valid probability vector,
        i.e., sum(x) = 1 and all x_i >= 0.

    Returns:
    float
        The value of the PDF at x.
    """
    if not np.all(np.isclose(np.sum(x), 1)) or np.any(x < 0):
        raise ValueError("x must be a valid probability vector.")

    # Calculate the normalization constant
    norm_const = gamma(np.sum(alpha)) / np.prod(gamma(alpha))

    # Calculate the PDF
    return norm_const * np.prod(x ** (alpha - 1))

# Example usage:
alpha = [2, 3, 5]  # Concentration parameters
x = [0.1, 0.2, 0.7]  # A valid probability vector
pdf_value = dirichlet_pdf(alpha, x)
print(f"PDF value at {x}: {pdf_value}")
