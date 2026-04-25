
import numpy as np
from scipy.special import gammaln

def dirichlet_pdf(x, alpha):
    """
    Calculate the PDF of the Dirichlet distribution.

    Parameters:
    x : array-like
        Points at which to evaluate the PDF (must be non-negative and sum to 1).
    alpha : array-like
        Concentration parameters of the Dirichlet distribution.

    Returns:
    float
        The value of the PDF at the point x.
    """

    # Ensure x and alpha are numpy arrays
    x = np.asarray(x)
    alpha = np.asarray(alpha)

    # Check that x is a valid Dirichlet point
    if np.any(x < 0) or not np.isclose(np.sum(x), 1):
        raise ValueError("x must be non-negative and sum to 1.")

    # Calculate the PDF using the formula
    numerator = np.prod(x ** (alpha - 1))
    denominator = np.exp(gammaln(np.sum(alpha)) - np.sum(gammaln(alpha)))

    return numerator / denominator

# Example usage
alpha = [2, 3, 4]  # Concentration parameters
x = [0.1, 0.3, 0.6]  # Probability vector

pdf_value = dirichlet_pdf(x, alpha)
print("PDF value:", pdf_value)
