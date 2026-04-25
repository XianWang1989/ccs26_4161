
import numpy as np
from scipy.special import gammaln

def dirichlet_pdf(alpha, x):
    """
    Calculate the PDF of the Dirichlet distribution.

    Parameters:
    alpha: array-like, shape (K,)
        Concentration parameters of the Dirichlet distribution.
    x: array-like, shape (K,)
        A point at which to evaluate the PDF. Must sum to 1.

    Returns:
    float
        The value of the PDF at point x.
    """
    if not np.isclose(sum(x), 1):
        raise ValueError("x must sum to 1.")
    if any(x < 0):
        return 0.0  # PDF is zero for negative x values.

    K = len(alpha)
    return (np.prod(x ** (alpha - 1)) /
            np.exp(gammaln(np.sum(alpha)) - np.sum(gammaln(alpha))))

# Example usage
alpha = np.array([1, 2, 3])
x = np.array([0.2, 0.5, 0.3])  # This should sum to 1
pdf_value = dirichlet_pdf(alpha, x)
print(f"The PDF value at {x} for alpha {alpha} is {pdf_value:.4f}.")
