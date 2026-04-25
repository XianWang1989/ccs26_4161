
import numpy as np
from scipy.special import gammaln

def dirichlet_pdf(alpha, x):
    """
    Calculate the PDF of the Dirichlet distribution.

    Parameters:
        alpha (array-like): The concentration parameters of the Dirichlet distribution.
        x (array-like): The point at which to evaluate the PDF (should sum to 1).

    Returns:
        float: The value of the PDF at x.
    """
    # Ensure x is a numpy array
    x = np.asarray(x)

    # Check if x sums to 1
    if not np.isclose(np.sum(x), 1):
        raise ValueError("Input x must sum to 1.")

    # Calculate the PDF
    K = len(alpha)
    numerator = np.prod(x ** (alpha - 1))
    denominator = np.exp(gammaln(np.sum(alpha)) - np.sum(gammaln(alpha)))

    return numerator / denominator

# Example usage
alpha = [1, 1, 1]  # Concentration parameters
x = [0.2, 0.5, 0.3]  # A point in the simplex where x1 + x2 + x3 = 1
pdf_value = dirichlet_pdf(alpha, x)
print(f"The PDF of the Dirichlet distribution at {x} is: {pdf_value}")
