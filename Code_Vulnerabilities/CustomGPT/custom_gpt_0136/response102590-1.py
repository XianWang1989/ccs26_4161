
import numpy as np
from scipy.special import gammaln

def dirichlet_pdf(alpha, x):
    """
    Calculate the PDF of the Dirichlet distribution.

    Parameters:
        alpha: array-like, shape (K, )
            The concentration parameters of the Dirichlet distribution.
        x: array-like, shape (K, )
            The point at which to evaluate the PDF (must sum to 1).

    Returns:
        float
            The value of the Dirichlet PDF at x.
    """
    K = len(alpha)
    if not np.isclose(np.sum(x), 1):
        raise ValueError("x must sum to 1")

    return (np.prod(x**(alpha - 1)) / np.exp(gammaln(np.sum(alpha)))) * np.prod(np.exp(gammaln(alpha)))

# Example usage:
alpha = np.array([1.0, 2.0, 3.0])  # Concentration parameters
x = np.array([0.2, 0.5, 0.3])       # Point to evaluate (must sum to 1)

pdf_value = dirichlet_pdf(alpha, x)
print("Dirichlet PDF value:", pdf_value)
