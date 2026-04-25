
import numpy as np
from scipy.special import gammaln

def dirichlet_pdf(x, alpha):
    """
    Calculate the pdf of the Dirichlet distribution.

    Parameters:
    x : array_like
        An array of probabilities (must sum to 1 and be in [0, 1])
    alpha : array_like
        The alpha parameters of the Dirichlet distribution

    Returns:
    float
        The pdf of the Dirichlet distribution at x
    """
    if np.sum(x) != 1 or np.any(x < 0):
        raise ValueError("x must sum to 1 and be non-negative.")

    # Compute the pdf
    a_sum = np.sum(alpha)
    pdf = np.exp(np.sum(gammaln(alpha)) - gammaln(a_sum) + np.sum((alpha - 1) * np.log(x)))

    return pdf

# Example usage
alpha = np.array([2, 3, 5])  # Parameters for the Dirichlet distribution
x = np.array([0.2, 0.3, 0.5]) # Probabilities that sum to 1

pdf_value = dirichlet_pdf(x, alpha)
print("PDF value:", pdf_value)
