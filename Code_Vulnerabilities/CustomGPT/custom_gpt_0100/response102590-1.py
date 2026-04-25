
import numpy as np
from scipy.special import gammaln

def dirichlet_pdf(alpha, x):
    """
    Calculate the PDF of the Dirichlet distribution.

    Parameters:
    alpha : array-like, shape (K,)
        The concentration parameters (must be positive).
    x : array-like, shape (K,)
        The point at which to evaluate the PDF (must sum to 1 and be in (0, 1)).

    Returns:
    float
        The value of the PDF at x.
    """
    # Check for valid input
    if any(a <= 0 for a in alpha):
        raise ValueError("All concentration parameters must be positive.")
    if not np.isclose(np.sum(x), 1) or any(x < 0) or any(x > 1):
        raise ValueError("x must be a valid probability vector.")

    K = len(alpha)
    log_pdf = (gammaln(np.sum(alpha)) - 
                np.sum(gammaln(alpha)) +
                np.sum((alpha - 1) * np.log(x)))
    return np.exp(log_pdf)

# Example usage
alpha = [2, 3, 5]  # Example concentration parameters
x = [0.2, 0.3, 0.5]  # A valid point in the simplex (0,1) and sums to 1
pdf_value = dirichlet_pdf(alpha, x)
print(f"The PDF of the Dirichlet distribution at {x} is: {pdf_value}")
