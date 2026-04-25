
import numpy as np
from scipy.special import gammaln

def dirichlet_pdf(x, alpha):
    """
    Calculate the PDF of the Dirichlet distribution.

    Parameters:
    x (array-like): Points at which to evaluate the PDF (must sum to 1 and >= 0).
    alpha (array-like): Concentration parameters.

    Returns:
    float: The value of the PDF at x.
    """
    if np.sum(x) != 1 or np.any(x < 0):
        raise ValueError("x should be a probability vector that sums to 1 with all elements >= 0")

    log_pdf = (gammaln(np.sum(alpha)) 
                - np.sum(gammaln(alpha)) 
                + np.sum((alpha - 1) * np.log(x)))

    return np.exp(log_pdf)

# Example usage
alpha = [1, 2, 3]  # Example concentration parameters
x = [0.2, 0.5, 0.3]  # Probability vector (must sum to 1)

pdf_value = dirichlet_pdf(x, alpha)
print("PDF value:", pdf_value)
