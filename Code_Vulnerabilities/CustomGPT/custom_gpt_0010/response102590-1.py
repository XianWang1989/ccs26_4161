
import numpy as np
from scipy.special import gammaln

def dirichlet_pdf(alpha, x):
    """
    Calculate the pdf of the Dirichlet distribution.

    Parameters:
    alpha : array_like
        The concentration parameters (shape) of the Dirichlet distribution.
    x : array_like
        The probabilities at which to evaluate the pdf. It should sum to 1.

    Returns:
    float
        The value of the pdf at x.
    """
    if not np.isclose(np.sum(x), 1):
        raise ValueError("The elements of x must sum to 1.")

    return np.exp(np.sum(gammaln(alpha)) - gammaln(np.sum(alpha)) + np.sum((alpha - 1) * np.log(x)))

# Example usage
alpha = np.array([1, 1, 1])  # Uniform Dirichlet distribution
x = np.array([0.2, 0.3, 0.5])  # Example probabilities that sum to 1

pdf_value = dirichlet_pdf(alpha, x)
print("PDF value:", pdf_value)
