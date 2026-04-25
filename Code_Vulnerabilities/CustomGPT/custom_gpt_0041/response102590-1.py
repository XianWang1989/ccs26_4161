
import numpy as np
from scipy.special import gammaln

def dirichlet_pdf(x, alpha):
    """
    Calculate the PDF of the Dirichlet distribution.

    Parameters:
    x (array-like): Values for which to compute the PDF (should sum to 1).
    alpha (array-like): Concentration parameters.

    Returns:
    float: The value of the PDF at x.
    """
    if not np.isclose(np.sum(x), 1):
        raise ValueError("Input x must sum to 1.")

    log_pdf = (gammaln(np.sum(alpha)) -
                np.sum(gammaln(alpha)) +
                np.sum((alpha - 1) * np.log(x)))

    return np.exp(log_pdf)

# Example usage
alpha = [2.0, 3.0, 5.0]  # Example concentration parameters
x = [0.1, 0.2, 0.7]      # Example x that sums to 1

pdf_value = dirichlet_pdf(x, alpha)
print(f"PDF value: {pdf_value}")
