
import numpy as np
from scipy.special import gammaln

def dirichlet_pdf(x, alpha):
    """
    Calculate the pdf of the Dirichlet distribution.

    Parameters:
    x : array-like
        A vector of probabilities (should sum to 1).
    alpha : array-like
        The concentration parameter of the Dirichlet distribution.

    Returns:
    float
        The value of the pdf.
    """
    if not np.isclose(np.sum(x), 1):
        raise ValueError("The elements of x must sum to 1.")

    return np.exp(np.sum(gammaln(alpha)) - gammaln(np.sum(alpha)) + 
                     np.sum((alpha - 1) * np.log(x)))

# Example usage
alpha = np.array([2, 3, 5])
x = np.array([0.1, 0.2, 0.7])  # Should sum to 1
pdf_value = dirichlet_pdf(x, alpha)
print(f"The pdf value of the Dirichlet distribution is: {pdf_value}")
