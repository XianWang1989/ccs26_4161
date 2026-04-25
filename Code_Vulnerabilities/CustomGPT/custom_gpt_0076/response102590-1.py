
import numpy as np
from scipy.special import gammaln

def dirichlet_pdf(alpha, x):
    """
    Calculate the PDF of the Dirichlet distribution.

    Parameters:
    alpha (array): Concentration parameter (shape).
    x (array): Point at which to evaluate the PDF (should sum to 1).

    Returns:
    float: The value of the PDF at point x.
    """
    # Ensure x is a valid probability vector
    if not np.allclose(np.sum(x), 1):
        raise ValueError("The elements of x must sum to 1.")
    if np.any(x < 0):
        raise ValueError("Elements of x must be non-negative.")

    # Calculate the PDF
    alpha_sum = np.sum(alpha)
    log_pdf = (gammaln(alpha_sum) - np.sum(gammaln(alpha)) +
                np.sum((alpha - 1) * np.log(x)))
    return np.exp(log_pdf)

# Example usage
alpha = np.array([1.0, 2.0, 3.0])
x = np.array([0.1, 0.2, 0.7])  # should sum to 1
pdf_value = dirichlet_pdf(alpha, x)
print("PDF value:", pdf_value)
