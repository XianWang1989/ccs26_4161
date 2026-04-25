
import numpy as np
from scipy.special import gammaln

def dirichlet_pdf(alpha, x):
    """
    Calculate the pdf of the Dirichlet distribution.

    Parameters:
    alpha : array-like
        The parameter of the Dirichlet distribution (must be positive).
    x : array-like
        The point(s) at which to evaluate the pdf (must be a valid probability vector).

    Returns:
    float : The value of the pdf at x.
    """
    # Ensure that x is a valid probability vector
    if not np.all(x >= 0) or not np.isclose(np.sum(x), 1):
        raise ValueError("x must be a probability vector (non-negative and sum to 1)")

    # The Dirichlet pdf formula
    alpha0 = np.sum(alpha)
    return np.exp(np.sum(gammaln(alpha)) - gammaln(alpha0) + (alpha - 1) * np.log(x))

# Example usage
alpha = [2, 5, 3]  # Example parameters for the Dirichlet distribution
x = [0.2, 0.5, 0.3]  # A valid probability vector

pdf_value = dirichlet_pdf(alpha, x)
print("The pdf of the Dirichlet distribution at x is:", pdf_value)
