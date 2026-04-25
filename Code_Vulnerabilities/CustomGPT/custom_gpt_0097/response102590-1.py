
import numpy as np
from scipy.special import gammaln

def dirichlet_pdf(alpha, x):
    """
    Calculate the PDF of the Dirichlet distribution.

    Parameters:
    alpha : array-like, shape (K,)
        The parameters of the Dirichlet distribution.
    x : array-like, shape (K,)
        A probability vector (sum(x) = 1).

    Returns:
    float
        The value of the PDF at x.
    """
    if sum(x) != 1 or any(i < 0 for i in x):
        raise ValueError("x must be a probability vector that sums to 1.")

    K = len(alpha)
    return np.exp(gammaln(sum(alpha)) - np.sum(gammaln(alpha)) + np.sum((alpha - 1) * np.log(x)))

# Example usage
alpha = [2, 3, 5]
x = [0.1, 0.3, 0.6]
pdf_value = dirichlet_pdf(alpha, x)
print("PDF value:", pdf_value)
