
import numpy as np
from scipy.special import gamma

def dirichlet_pdf(alpha, x):
    """
    Calculate the pdf of the Dirichlet distribution.

    Parameters:
    alpha : array-like
        Concentration parameters of the Dirichlet distribution.
    x : array-like
        Points at which to evaluate the pdf (must sum to 1 and be >= 0).

    Returns:
    float
        Probability density at x.
    """
    if not np.isclose(np.sum(x), 1):
        raise ValueError("The sum of x must be 1.")
    if np.any(x < 0):
        raise ValueError("All elements of x must be non-negative.")

    # Calculate the numerator: product of x[i]^(alpha[i] - 1)
    numerator = np.prod(x ** (alpha - 1))

    # Calculate the denominator: gamma(sum(alpha)) / product(gamma(alpha))
    denominator = gamma(np.sum(alpha)) / np.prod(gamma(alpha))

    return numerator / denominator

# Example usage
alpha = [2, 3, 5]
x = [0.2, 0.5, 0.3]
pdf_value = dirichlet_pdf(alpha, x)
print("Dirichlet PDF value:", pdf_value)
