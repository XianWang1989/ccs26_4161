
import numpy as np
from scipy.special import gammaln

def dirichlet_pdf(x, alpha):
    """
    Calculate the pdf of the Dirichlet distribution.

    Parameters:
    x : array-like, shape (K,)
        Input parameters (should sum to 1).
    alpha : array-like, shape (K,)
        Parameter of the Dirichlet distribution.

    Returns:
    float
        The pdf value.
    """
    if np.any(x < 0) or np.sum(x) != 1:
        raise ValueError("Input x must be non-negative and sum to 1.")
    if len(x) != len(alpha):
        raise ValueError("Dimensions of x and alpha must match.")

    return np.exp(np.sum(gammaln(alpha)) - gammaln(np.sum(alpha)) + np.sum((alpha - 1) * np.log(x)))

# Example usage:
alpha = np.array([1.0, 2.0, 3.0])   # Parameters of the Dirichlet distribution
x = np.array([0.2, 0.3, 0.5])        # Must sum to 1

pdf_value = dirichlet_pdf(x, alpha)
print("PDF value:", pdf_value)
