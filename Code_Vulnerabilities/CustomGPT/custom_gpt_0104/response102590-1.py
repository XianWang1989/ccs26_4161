
import numpy as np
from scipy.special import gamma

def dirichlet_pdf(x, alpha):
    """
    Calculate the pdf of Dirichlet distribution for a given x and alpha.

    Parameters:
    x: array_like
        A point at which to evaluate the pdf, should sum to 1.
    alpha: array_like
        The concentration parameters of the Dirichlet distribution.

    Returns:
    float
        The value of the pdf at point x.
    """
    if not np.isclose(np.sum(x), 1):
        raise ValueError("The elements of x must sum to 1")

    if len(x) != len(alpha):
        raise ValueError("x and alpha must have the same length")

    numerator = np.prod(x**(alpha - 1))
    denominator = np.prod(gamma(alpha)) / gamma(np.sum(alpha))

    return numerator / denominator

# Example usage
alpha = [2, 3, 5]  # Concentration parameters
x = [0.2, 0.5, 0.3]  # Example point (must sum to 1)

pdf_value = dirichlet_pdf(x, alpha)
print(f'The pdf value of Dirichlet distribution at x={x} with alpha={alpha} is: {pdf_value}')
