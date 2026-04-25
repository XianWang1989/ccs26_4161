
import numpy as np
from scipy.special import gammaln

def dirichlet_pdf(x, alpha):
    """
    Calculate the PDF of the Dirichlet distribution.

    Parameters:
    x (array-like): A 1D array of probabilities (should sum to 1).
    alpha (array-like): Parameter of the Dirichlet distribution (concentration parameters).

    Returns:
    float: The value of the pdf at x.
    """
    if not np.isclose(np.sum(x), 1):
        raise ValueError("Input probabilities must sum to 1.")

    log_pdf = (gammaln(np.sum(alpha))
                - np.sum(gammaln(alpha))
                + np.sum((alpha - 1) * np.log(x)))
    return np.exp(log_pdf)

# Example usage
alpha = [2.0, 3.0, 5.0]
x = [0.1, 0.2, 0.7]  # Should sum to 1
pdf_value = dirichlet_pdf(x, alpha)
print(f"The Dirichlet PDF value is: {pdf_value}")
