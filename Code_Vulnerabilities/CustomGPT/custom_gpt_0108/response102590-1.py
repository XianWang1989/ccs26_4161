
import numpy as np
from scipy.special import gammaln

def dirichlet_pdf(x, alpha):
    """
    Calculate the PDF of the Dirichlet distribution.

    Parameters:
    x (array-like): A 1D array of probabilities (must sum to 1)
    alpha (array-like): Concentration parameters (must be positive)

    Returns:
    float: The PDF value at x
    """
    if not np.isclose(np.sum(x), 1):
        raise ValueError("The elements of x must sum to 1.")
    if any(a <= 0 for a in alpha):
        raise ValueError("All concentration parameters must be positive.")

    d = len(alpha)
    numerator = np.prod(x ** (alpha - 1))
    denominator = np.exp(gammaln(np.sum(alpha)) - np.sum(gammaln(alpha)))

    return numerator / denominator

# Example usage
alpha = [2, 3, 5]  # Concentration parameters
x = [0.1, 0.3, 0.6]  # Example probabilities

pdf_value = dirichlet_pdf(x, alpha)
print("PDF Value:", pdf_value)
