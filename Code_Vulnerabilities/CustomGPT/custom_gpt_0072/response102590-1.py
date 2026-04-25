
import numpy as np
from scipy.special import gammaln

def dirichlet_pdf(alpha, x):
    """
    Compute the pdf of the Dirichlet distribution.

    Parameters:
    alpha : array-like, shape (K,)
        Parameter of the Dirichlet distribution (alpha > 0).
    x : array-like, shape (K,)
        Point at which to evaluate the pdf (0 < x_i < 1, sum(x) = 1).

    Returns:
    float
        The value of the pdf evaluated at x.
    """
    if np.any(x < 0) or np.any(x > 1) or not np.isclose(np.sum(x), 1):
        return 0.0  # x must be a valid probability vector
    K = len(alpha)
    return np.exp(np.sum(gammaln(alpha)) - gammaln(np.sum(alpha)) + 
                   np.sum((alpha - 1) * np.log(x)))

# Example usage
alpha = [1, 1, 1]  # Parameters (each alpha > 0)
x = [0.2, 0.5, 0.3]  # A valid probability vector
pdf_value = dirichlet_pdf(alpha, x)
print(f"The pdf value at {x} is: {pdf_value}")
