
import numpy as np
from scipy.special import gammaln

def dirichlet_pdf(x, alpha):
    """
    Calculate the pdf of the Dirichlet distribution.

    Parameters:
    x : array-like, shape (k,)
        The input probabilities (should sum to 1)
    alpha : array-like, shape (k,)
        The concentration parameters (alpha > 0)

    Returns:
    pdf : float
        The probability density of the Dirichlet distribution at x
    """
    if not np.all(np.isclose(np.sum(x), 1)) or np.any(x < 0):
        raise ValueError("Input x must be a probability distribution (sum to 1 and non-negative).")

    if np.any(alpha <= 0):
        raise ValueError("Concentration parameters (alpha) must be positive.")

    k = len(alpha)
    numerator = np.prod(x ** (alpha - 1))
    denominator = np.exp(gammaln(np.sum(alpha)) - np.sum(gammaln(alpha)))

    return numerator / denominator

# Example usage
alpha = [1, 2, 3]  # concentration parameters
x = [0.2, 0.3, 0.5]  # probabilities summing to 1

pdf_value = dirichlet_pdf(x, alpha)
print("Dirichlet PDF value:", pdf_value)
