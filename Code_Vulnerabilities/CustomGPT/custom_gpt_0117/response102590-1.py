
import numpy as np
from scipy.special import gammaln

def dirichlet_pdf(alpha, x):
    """
    Calculate the pdf of the Dirichlet distribution.

    Parameters:
    alpha : array-like
        The parameters (alpha) of the Dirichlet distribution.
    x : array-like
        The input point where the pdf should be calculated (must sum to 1).

    Returns:
    float
        The value of the pdf at point x.
    """
    if np.sum(x) != 1:
        raise ValueError("Input x must sum to 1.")

    if np.any(x < 0):
        return 0.0  # The pdf is zero for x < 0

    alpha = np.asarray(alpha)
    x = np.asarray(x)

    # Compute the log pdf
    log_pdf = (gammaln(np.sum(alpha)) 
                - np.sum(gammaln(alpha)) 
                + np.sum((alpha - 1) * np.log(x)))

    return np.exp(log_pdf)

# Example parameters and input
alpha = [2, 3, 4]
x = [0.2, 0.3, 0.5]  # This should sum to 1

# Calculate the pdf
pdf_value = dirichlet_pdf(alpha, x)
print(f"Dirichlet pdf value: {pdf_value}")
