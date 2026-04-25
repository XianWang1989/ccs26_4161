
import numpy as np
from scipy.special import gammaln

def dirichlet_pdf(x, alpha):
    """
    Calculate the PDF of the Dirichlet distribution.

    Parameters:
    x : array-like
        Array of probabilities (must sum to 1 and all elements must be > 0)
    alpha : array-like
        Concentration parameters (should have the same length as x)

    Returns:
    float
        The value of the PDF at x
    """
    # Ensure x is a numpy array
    x = np.array(x)
    alpha = np.array(alpha)

    # Check conditions
    if not np.all(x > 0) or not np.isclose(np.sum(x), 1):
        raise ValueError("x must contain positive probabilities that sum to 1.")

    if x.shape != alpha.shape:
        raise ValueError("x and alpha must have the same shape.")

    # Calculate the PDF using the Dirichlet formula
    numerator = np.prod(x**(alpha - 1))
    denominator = np.exp(gammaln(np.sum(alpha)) - np.sum(gammaln(alpha)))

    return numerator / denominator

# Example usage
alpha = [1.0, 1.0, 1.0]  # Uniform distribution
x = [0.2, 0.3, 0.5]      # Probabilities
pdf_value = dirichlet_pdf(x, alpha)
print("PDF value:", pdf_value)
