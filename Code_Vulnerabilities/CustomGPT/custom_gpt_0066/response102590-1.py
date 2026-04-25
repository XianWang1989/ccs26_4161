
import numpy as np
from scipy.special import gammaln

def dirichlet_pdf(alpha, x):
    """
    Calculate the PDF of the Dirichlet distribution.

    Parameters:
    alpha (array-like): Parameters of the Dirichlet distribution.
    x (array-like): Points at which to evaluate the PDF (should sum to 1).

    Returns:
    float: PDF value at point x.
    """
    if np.sum(x) != 1.0:
        raise ValueError("x must sum to 1.")
    if any(x < 0):
        return 0  # PDF is zero if any element of x is negative

    a = np.array(alpha)
    return np.exp(np.sum(gammaln(a)) - gammaln(np.sum(a)) + np.sum((a - 1) * np.log(x)))

# Example usage
alpha = [2, 3, 5]
x = [0.2, 0.5, 0.3]
pdf_value = dirichlet_pdf(alpha, x)
print("PDF value:", pdf_value)
