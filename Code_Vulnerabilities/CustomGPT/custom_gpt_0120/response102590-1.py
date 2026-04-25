
import numpy as np
from scipy.special import gammaln

def dirichlet_pdf(alpha, x):
    """
    Calculate the PDF of the Dirichlet distribution.

    Parameters:
    alpha : array-like
        The parameters of the Dirichlet distribution (must be positive).
    x : array-like
        The probability vector (must sum to 1 and be positive).

    Returns:
    float
        The value of the PDF at the given point.
    """
    if np.any(x < 0) or np.any(x > 1) or not np.isclose(np.sum(x), 1):
        raise ValueError("x must be a probability vector summing to 1.")

    alpha = np.asarray(alpha)
    x = np.asarray(x)

    # Calculate the PDF
    return np.exp(np.sum(gammaln(alpha)) - gammaln(np.sum(alpha)) +
                   np.sum((alpha - 1) * np.log(x)))

# Example usage
alpha = [2, 3, 5]  # Dirichlet parameters
x = [0.1, 0.2, 0.7]  # Probability vector
pdf_value = dirichlet_pdf(alpha, x)
print("PDF value:", pdf_value)
