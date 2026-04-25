
import numpy as np
from scipy.special import gammaln

def dirichlet_pdf(alpha, x):
    """
    Calculate the PDF of the Dirichlet distribution.

    Parameters:
    alpha (array-like): Concentration parameters (must be positive).
    x (array-like): Points at which to calculate the PDF (must sum to 1 and be in [0, 1]).

    Returns:
    float: Value of the PDF at x.
    """
    if np.any(x < 0) or np.sum(x) != 1:
        raise ValueError("x must be a valid probability vector (non-negative and sums to 1).")

    alpha = np.asarray(alpha)
    K = len(alpha)

    # Calculate the PDF
    numerator = np.prod(x ** (alpha - 1))
    denominator = np.exp(gammaln(np.sum(alpha)) - np.sum(gammaln(alpha)))

    return numerator / denominator

# Example usage
alpha = [2, 5, 3]
x = [0.1, 0.2, 0.7]
pdf_value = dirichlet_pdf(alpha, x)
print(f"PDF value: {pdf_value}")
