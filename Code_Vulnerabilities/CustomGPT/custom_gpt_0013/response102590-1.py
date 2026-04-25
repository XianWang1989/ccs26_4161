
import numpy as np
from scipy.special import gamma

def dirichlet_pdf(x, alpha):
    """
    Calculate the pdf of the Dirichlet distribution.

    Parameters:
    x : array_like
        A point or points at which to evaluate the pdf. Must sum to 1.
    alpha : array_like
        The concentration parameters of the Dirichlet distribution.

    Returns:
    float
        The pdf value at x.
    """
    # Check if x sums to 1
    if not np.isclose(np.sum(x), 1):
        raise ValueError("The elements of x must sum to 1.")

    # Calculate the pdf
    numerator = np.prod(x ** (alpha - 1))
    denominator = gamma(np.sum(alpha)) / np.prod(gamma(alpha))

    return numerator / denominator

# Example usage
alpha = [1.0, 2.0, 3.0]  # Concentration parameters
x = [0.2, 0.5, 0.3]      # Point at which to evaluate the pdf

pdf_value = dirichlet_pdf(x, alpha)
print(f"The PDF of the Dirichlet distribution at {x} is {pdf_value:.4f}")
