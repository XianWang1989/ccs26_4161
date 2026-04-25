
import numpy as np
from scipy.special import gamma, gammaln

def dirichlet_pdf(x, alpha):
    """Calculate the PDF of the Dirichlet distribution.

    Parameters:
        x (array-like): Points at which to evaluate the PDF. Should sum to 1.
        alpha (array-like): Parameter of the Dirichlet distribution.

    Returns:
        float: PDF value at x.
    """
    # Ensure x is a numpy array
    x = np.asarray(x)
    alpha = np.asarray(alpha)

    # Check if x sums to 1
    if not np.isclose(np.sum(x), 1):
        raise ValueError("x must sum to 1.")

    # Calculate the PDF
    log_pdf = (
        gammaln(np.sum(alpha)) -
        np.sum(gammaln(alpha)) +
        np.sum((alpha - 1) * np.log(x))
    )
    return np.exp(log_pdf)

# Example usage
alpha = [2.0, 5.0, 1.0]
x = [0.1, 0.7, 0.2]  # Should sum to 1
pdf_value = dirichlet_pdf(x, alpha)
print("PDF value:", pdf_value)
