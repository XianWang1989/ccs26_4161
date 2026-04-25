
import numpy as np
from scipy.special import gamma

def dirichlet_pdf(x, alpha):
    """
    Calculate the pdf of the Dirichlet distribution.

    Parameters:
    x : array-like, shape (k,)
        Probabilities (must sum to 1).
    alpha : array-like, shape (k,)
        Concentration parameters.

    Returns:
    float
        Value of the pdf.
    """
    # Check if x is a valid probability vector
    if np.any(x < 0) or not np.isclose(np.sum(x), 1):
        raise ValueError("Input must be a probability vector that sums to 1.")

    # Calculate the normalizing constant
    B_alpha = np.prod(gamma(alpha)) / gamma(np.sum(alpha))

    # Calculate the pdf
    return (np.prod(x**(alpha - 1))) / B_alpha

# Example usage
x = np.array([0.2, 0.5, 0.3])
alpha = np.array([1, 1, 1])
print("PDF Value:", dirichlet_pdf(x, alpha))
