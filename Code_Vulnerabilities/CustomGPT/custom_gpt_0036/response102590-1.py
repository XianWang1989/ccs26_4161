
import numpy as np
from scipy.special import gamma

def dirichlet_pdf(x, alpha):
    """
    Calculate the pdf of the Dirichlet distribution.

    Parameters:
    x : array-like, shape (K,)
        The input probabilities vector (should sum to 1).
    alpha : array-like, shape (K,)
        The concentration parameters of the Dirichlet distribution.

    Returns:
    pdf : float
        The probability density function value at x.
    """
    # Make sure the input probabilities sum to 1
    if not np.isclose(np.sum(x), 1):
        raise ValueError("The components of x must sum to 1.")

    # Number of dimensions
    K = len(alpha)

    # Compute the normalization constant
    norm_const = gamma(np.sum(alpha)) / np.prod(gamma(alpha))

    # Calculate the pdf
    pdf = (np.prod(x ** (alpha - 1))) / norm_const

    return pdf

# Example usage
alpha = [2.0, 3.0, 5.0] # Concentration parameters
x = [0.2, 0.3, 0.5]     # Probability vector (should sum to 1)

pdf_value = dirichlet_pdf(x, alpha)
print("The pdf of the Dirichlet distribution is:", pdf_value)
