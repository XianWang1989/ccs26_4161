
import numpy as np
from scipy.special import gammaln

def dirichlet_pdf(alpha, x):
    """
    Calculate the PDF of the Dirichlet distribution.

    Parameters:
    alpha (array-like): The concentration parameters of the Dirichlet distribution.
    x (array-like): A point at which to evaluate the PDF. Should sum to 1 and be non-negative.

    Returns:
    float: The value of the PDF at point x.
    """
    if np.any(x < 0) or not np.isclose(np.sum(x), 1):
        return 0.0  # Out of support

    alpha = np.asarray(alpha)
    x = np.asarray(x)

    # Compute the normalization constant
    normalization = gammaln(np.sum(alpha)) - np.sum(gammaln(alpha))

    # Compute the log PDF
    log_pdf = normalization + np.sum((alpha - 1) * np.log(x))

    return np.exp(log_pdf)

# Example usage
alpha = [2.0, 3.0, 5.0]  # Concentration parameters
x = [0.1, 0.2, 0.7]      # Point in the simplex

pdf_value = dirichlet_pdf(alpha, x)
print(f"The PDF value of the Dirichlet distribution at {x} is: {pdf_value}")
