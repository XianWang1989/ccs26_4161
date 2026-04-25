
import numpy as np
from scipy.special import gammaln

def dirichlet_pdf(alpha, x):
    """
    Calculate the pdf of the Dirichlet distribution.

    Parameters:
    alpha (array-like): Concentration parameters of the Dirichlet distribution.
    x (array-like): Probability vector, must sum to 1 and all elements must be non-negative.

    Returns:
    float: Probability density value.
    """
    if np.sum(x) != 1:
        raise ValueError("Input x must sum to 1.")
    if any(i < 0 for i in x):
        raise ValueError("All elements of x must be non-negative.")

    K = len(alpha)  # Dimension of the distribution
    norm_const = np.exp(gammaln(np.sum(alpha)) - np.sum(gammaln(alpha)))

    return norm_const * np.prod(x ** (alpha - 1))

# Example usage
alpha = [2, 5, 3]  # Concentration parameters
x = [0.2, 0.5, 0.3]  # Probability vector
pdf_value = dirichlet_pdf(alpha, x)
print("Dirichlet PDF value:", pdf_value)
