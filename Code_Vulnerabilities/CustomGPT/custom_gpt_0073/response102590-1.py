
import numpy as np
from scipy.special import gamma

def dirichlet_pdf(x, alpha):
    """
    Calculate the PDF of the Dirichlet distribution.

    Parameters:
    x : array-like, shape (K,)
        Input value where the PDF is calculated. Must sum to 1.
    alpha : array-like, shape (K,)
        Concentration parameters (must be positive).

    Returns:
    float
        PDF value at x.
    """
    if not np.isclose(np.sum(x), 1):
        raise ValueError("The sum of the input vector x must be 1.")

    if np.any(alpha <= 0):
        raise ValueError("All elements of alpha must be positive.")

    K = len(alpha)
    numerator = np.prod(np.power(x, alpha - 1))
    denominator = gamma(np.sum(alpha)) / np.prod(gamma(alpha))

    return numerator / denominator

# Example usage
alpha = [2, 3, 5]  # Concentration parameters
x = [0.1, 0.5, 0.4]  # Must sum to 1
pdf_value = dirichlet_pdf(x, alpha)
print(f"The PDF of the Dirichlet distribution at {x} with alpha {alpha} is {pdf_value:.5f}")
