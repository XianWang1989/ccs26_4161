
import numpy as np
from scipy.special import gammaln

def dirichlet_pdf(alpha, x):
    """
    Calculate the PDF of the Dirichlet distribution.

    Parameters:
    alpha (array-like): The concentration parameters of the Dirichlet distribution.
    x (array-like): The points at which to evaluate the PDF (must sum to 1 and be in [0, 1]).

    Returns:
    float: The value of the PDF at point x.
    """
    if not np.isclose(np.sum(x), 1):
        raise ValueError("The input x must sum to 1.")
    if any(x < 0) or any(x > 1):
        raise ValueError("All elements of x must be in the interval [0, 1].")

    a = np.array(alpha)
    return np.exp(np.sum(gammaln(a)) - gammaln(np.sum(a)) + np.sum((a - 1) * np.log(x)))

# Example usage
alpha = [2, 3, 5]  # Concentration parameters
x = [0.2, 0.5, 0.3]  # Point at which to calculate the PDF
pdf_value = dirichlet_pdf(alpha, x)
print(f"PDF value: {pdf_value}")
