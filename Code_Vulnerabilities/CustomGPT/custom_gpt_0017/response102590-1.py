
import numpy as np
from scipy.special import gammaln

def dirichlet_pdf(x, alpha):
    """
    Calculate the pdf of the Dirichlet distribution.

    Parameters:
    x : array-like
        A 1D array of probabilities (sum must equal 1).
    alpha : array-like
        Concentration parameters (must be positive).

    Returns:
    float
        The value of the pdf at x.
    """
    # Ensure x is a numpy array
    x = np.asarray(x)
    alpha = np.asarray(alpha)

    if not np.isclose(np.sum(x), 1):
        raise ValueError("The elements of x must sum to 1.")
    if np.any(alpha <= 0):
        raise ValueError("All concentration parameters must be positive.")

    # Calculate the pdf
    normalization_constant = np.exp(np.sum(gammaln(alpha)) - gammaln(np.sum(alpha)))
    pdf_value = normalization_constant * np.prod(x ** (alpha - 1))

    return pdf_value

# Example usage
alpha = [1, 2, 3]
x = [0.2, 0.5, 0.3]
pdf_value = dirichlet_pdf(x, alpha)
print("PDF value:", pdf_value)
