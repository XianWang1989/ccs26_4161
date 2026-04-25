
import numpy as np
from scipy.special import gammaln

def dirichlet_pdf(x, alpha):
    """
    Calculate the pdf of the Dirichlet distribution.

    Parameters:
    x : array-like, shape (k,)
        A point (k dimensions) in the distribution.
    alpha : array-like, shape (k,)
        The concentration parameters of the Dirichlet distribution.

    Returns:
    float
        The pdf value at point x.
    """
    if np.any(x < 0) or np.sum(x) != 1:
        return 0.0

    k = len(x)
    log_pdf = (gammaln(np.sum(alpha)) 
                - np.sum(gammaln(alpha)) 
                + np.sum((alpha - 1) * np.log(x)))
    return np.exp(log_pdf)

# Example usage
alpha = [2, 5, 3]  # concentration parameters
x = [0.2, 0.5, 0.3]  # point at which to evaluate the pdf

pdf_value = dirichlet_pdf(x, alpha)
print("PDF value:", pdf_value)
