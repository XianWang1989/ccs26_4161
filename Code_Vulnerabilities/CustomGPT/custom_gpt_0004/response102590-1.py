
import numpy as np
from scipy.special import gammaln

def dirichlet_pdf(alpha, x):
    """
    Calculate the pdf of the Dirichlet distribution.

    Parameters:
    alpha : array-like
        The concentration parameters of the Dirichlet distribution.
    x : array-like
        Points at which to evaluate the pdf. Must sum to 1.

    Returns:
    float
        The value of the pdf at x.
    """
    if not np.isclose(np.sum(x), 1):
        raise ValueError("The elements of x must sum to 1.")

    alpha = np.asarray(alpha)
    x = np.asarray(x)

    log_pdf = (gammaln(np.sum(alpha)) - 
                np.sum(gammaln(alpha)) + 
                np.sum((alpha - 1) * np.log(x)))

    return np.exp(log_pdf)

# Example usage
alpha = [2, 3, 5]  # Concentration parameters
x = [0.1, 0.2, 0.7]  # Sample point (should sum to 1)

pdf_value = dirichlet_pdf(alpha, x)
print(f"The pdf value at x is: {pdf_value}")
