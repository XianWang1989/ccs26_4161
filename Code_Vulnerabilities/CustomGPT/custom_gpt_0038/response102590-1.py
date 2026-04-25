
import numpy as np
from scipy.special import gammaln

def dirichlet_pdf(alpha, x):
    """Calculate the PDF of the Dirichlet distribution.

    Parameters:
    alpha (list or np.ndarray): The parameters of the Dirichlet distribution.
    x (list or np.ndarray): The points at which to evaluate the PDF.

    Returns:
    float: The value of the PDF at x.
    """
    if len(alpha) != len(x) or np.sum(x) != 1 or np.any(x < 0):
        raise ValueError("x must be a probability vector (sum to 1 and non-negative).")

    a_sum = np.sum(alpha)
    log_pdf = (gammaln(a_sum) - np.sum(gammaln(alpha)) +
                np.sum((alpha - 1) * np.log(x)))
    return np.exp(log_pdf)

# Example usage
alpha = [2, 5, 3]  # Parameters
x = [0.1, 0.6, 0.3]  # A valid probability vector

pdf_value = dirichlet_pdf(alpha, x)
print(f"The PDF value is: {pdf_value}")
