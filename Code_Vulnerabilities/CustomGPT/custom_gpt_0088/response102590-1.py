
import numpy as np
from scipy.special import gammaln

def dirichlet_pdf(x, alpha):
    """
    Calculate the pdf of the Dirichlet distribution.

    Parameters:
        x (array-like): A vector of probabilities (must sum to 1, must be between 0 and 1).
        alpha (array-like): A vector of concentration parameters.

    Returns:
        float: The probability density function evaluated at x.
    """
    if not np.all(np.isclose(np.sum(x), 1)) or np.any(x < 0):
        raise ValueError("x must be a probability vector that sums to 1 and is non-negative.")

    k = len(alpha)
    normalization_const = gammaln(np.sum(alpha)) - np.sum(gammaln(alpha))
    pdf_value = np.exp(normalization_const + np.sum((alpha - 1) * np.log(x)))

    return pdf_value

# Example usage:
alpha_params = [2.0, 3.0, 4.0]
x_vector = [0.2, 0.5, 0.3]  # Must sum to 1
pdf_value = dirichlet_pdf(x_vector, alpha_params)
print("Dirichlet PDF:", pdf_value)
