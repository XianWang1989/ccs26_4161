
import numpy as np
from scipy.special import gamma

def dirichlet_pdf(alpha, x):
    """
    Calculate the PDF of the Dirichlet distribution.

    Parameters:
    alpha : array_like
        The concentration parameters of the Dirichlet distribution.
    x : array_like
        Probability vector (sum to 1 and all x_i >= 0).

    Returns:
    float
        The value of the PDF at x.
    """

    if not np.isclose(np.sum(x), 1):
        raise ValueError("x must sum to 1.")

    if np.any(x < 0):
        raise ValueError("All elements of x must be non-negative.")

    # Calculate the PDF using the formula
    numerator = np.prod(x**(alpha - 1))
    denominator = gamma(np.sum(alpha)) / np.prod(gamma(alpha))

    return numerator / denominator

# Example usage
alpha = np.array([2.0, 3.0, 4.0])
x = np.array([0.2, 0.3, 0.5])
pdf_value = dirichlet_pdf(alpha, x)
print(f"The PDF value for the Dirichlet distribution is: {pdf_value}")
