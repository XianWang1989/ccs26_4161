
import numpy as np
from scipy.special import gammaln
from scipy.stats import dirichlet

def dirichlet_pdf(alpha, x):
    """
    Calculate the PDF of the Dirichlet distribution.

    Parameters:
    alpha : array_like
        The concentration parameters of the Dirichlet distribution.
    x : array_like
        The point at which to evaluate the PDF. Should sum to 1.

    Returns:
    float
        The value of the PDF at x.
    """
    # Ensure x is a valid probability vector
    if not np.isclose(np.sum(x), 1):
        raise ValueError("The components of x must sum to 1.")

    # Calculate the PDF using the Dirichlet distribution
    return dirichlet.pdf(x, alpha)

# Example usage
alpha = [1, 2, 3]  # Concentration parameters
x = [0.1, 0.2, 0.7]  # Probability vector

pdf_value = dirichlet_pdf(alpha, x)
print(f"The PDF value is: {pdf_value}")
