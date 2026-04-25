
import numpy as np
from scipy.special import gammaln

def dirichlet_pdf(x, alpha):
    """
    Compute the PDF of the Dirichlet distribution.

    Parameters:
    x : array-like
        Point(s) at which to evaluate the PDF. Must sum to 1 and all x_i > 0.
    alpha : array-like
        Parameters of the Dirichlet distribution.

    Returns:
    float
        The value of the PDF at point x.
    """
    # Ensure that x is a numpy array
    x = np.asarray(x)
    alpha = np.asarray(alpha)

    if not np.all(x > 0) or not np.isclose(np.sum(x), 1):
        raise ValueError("x must sum to 1 and all elements must be greater than 0.")

    # Compute the PDF using the formula
    numerator = np.prod(x ** (alpha - 1))
    denominator = np.exp(gammaln(np.sum(alpha)) - np.sum(gammaln(alpha)))

    return numerator / denominator

# Example usage
alpha = [2, 3, 4]  # Parameters of the Dirichlet distribution
x = [0.2, 0.3, 0.5]  # Point where we evaluate the PDF

pdf_value = dirichlet_pdf(x, alpha)
print(f"The PDF value at {x} for Dirichlet distribution with alpha {alpha} is: {pdf_value}")
