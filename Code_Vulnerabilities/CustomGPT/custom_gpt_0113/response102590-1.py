
import numpy as np
from scipy.special import gamma

def dirichlet_pdf(x, alpha):
    """
    Calculate the probability density function of the Dirichlet distribution.

    Parameters:
    x : array-like
        A vector of probabilities (sum to 1).
    alpha : array-like
        The parameters of the Dirichlet distribution.

    Returns:
    float
        The pdf value.
    """
    # Check if x sums to 1
    if not np.isclose(np.sum(x), 1):
        raise ValueError("x must sum to 1.")

    k = len(alpha)
    numerator = np.prod([x_i ** (alpha_i - 1) for x_i, alpha_i in zip(x, alpha)])
    denominator = gamma(np.sum(alpha)) / np.prod([gamma(alpha_i) for alpha_i in alpha])

    return numerator / denominator

# Example usage
alpha = [2, 3, 5]
x = [0.1, 0.2, 0.7]  # Must sum to 1
pdf_value = dirichlet_pdf(x, alpha)
print("PDF of Dirichlet distribution:", pdf_value)
