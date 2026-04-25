
import numpy as np
from scipy.special import gammaln

def dirichlet_pdf(alpha, x):
    """
    Calculate the PDF of the Dirichlet distribution.

    Parameters:
    alpha : array-like
        Concentration parameters (must be positive).
    x : array-like
        Probability vectors (elements must be non-negative and sum to 1).

    Returns:
    float
        The value of the PDF at the point x.
    """
    if isinstance(alpha, (int, float)):
        alpha = np.array([alpha])
    if isinstance(x, (int, float)):
        x = np.array([x])

    # Check inputs
    if np.any(alpha <= 0) or np.any(x < 0) or not np.isclose(np.sum(x), 1):
        return 0

    # Calculate the PDF
    k = len(alpha)
    numerator = np.prod(x ** (alpha - 1))
    denominator = np.exp(gammaln(np.sum(alpha)) - np.sum(gammaln(alpha)))

    return numerator / denominator

# Example usage
alpha = [2, 5, 3]  # concentration parameters
x = [0.2, 0.5, 0.3]  # a probability vector summing to 1

pdf_value = dirichlet_pdf(alpha, x)
print(f"The PDF of the Dirichlet distribution at x is: {pdf_value}")
