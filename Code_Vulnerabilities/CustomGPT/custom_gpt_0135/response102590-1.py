
import numpy as np
from scipy.special import gamma

def dirichlet_pdf(x, alpha):
    """
    Calculate the PDF of the Dirichlet distribution.

    Parameters:
    x : array-like
        A point on which to evaluate the PDF. Must sum to 1 and be non-negative.
    alpha : array-like
        The concentration parameters (also called Dirichlet parameters).

    Returns:
    float
        The PDF value at x.
    """
    if np.any(x < 0) or not np.isclose(np.sum(x), 1):
        raise ValueError("x must be non-negative and sum to 1.")

    # Calculate the PDF using the Dirichlet formula
    numerator = np.prod(x ** (alpha - 1))
    denominator = gamma(np.sum(alpha)) / np.prod(gamma(alpha))

    return numerator / denominator

# Example usage
alpha = np.array([1.0, 2.0, 3.0])  # Concentration parameters
x = np.array([0.2, 0.3, 0.5])      # Point where we want the PDF

pdf_value = dirichlet_pdf(x, alpha)
print(f"Dirichlet PDF value: {pdf_value}")
