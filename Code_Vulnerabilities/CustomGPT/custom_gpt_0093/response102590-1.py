
import numpy as np
from scipy.special import gamma

def dirichlet_pdf(alpha, x):
    """
    Calculate the PDF of the Dirichlet distribution.

    Parameters:
    alpha: array-like, shape (K,)
        Concentration parameters of the Dirichlet distribution.
    x: array-like, shape (K,)
        Points at which to evaluate the PDF.

    Returns:
    float
        Value of the PDF at point x.
    """
    K = len(alpha)

    # Check that x sums to 1
    if not np.isclose(np.sum(x), 1):
        raise ValueError("The elements of x must sum to 1.")

    # Calculate the PDF
    numerator = np.prod(x ** (alpha - 1))
    denominator = np.prod(gamma(alpha)) / gamma(np.sum(alpha))

    return numerator / denominator

# Example usage
alpha = [2.0, 3.0, 5.0]
x = [0.1, 0.2, 0.7]  # should sum to 1
pdf_value = dirichlet_pdf(alpha, x)
print(f"The PDF value for the Dirichlet distribution is: {pdf_value}")
