
import numpy as np
from scipy.special import gamma

def dirichlet_pdf(alpha, x):
    """
    Calculate the PDF of the Dirichlet distribution.

    Parameters:
    alpha (array-like): The concentration parameters of the Dirichlet distribution.
    x (array-like): The input values (must be in the simplex).

    Returns:
    float: The value of the PDF at x.
    """
    if not np.all(np.isclose(np.sum(x), 1)) or np.any(x < 0):
        raise ValueError("x must be a probability vector (sum to 1 and non-negative).")

    # Compute the gamma function of the sum of alpha
    coeff = gamma(np.sum(alpha)) / np.prod(gamma(alpha))
    # Compute the PDF
    pdf_value = coeff * np.prod(x ** (alpha - 1))
    return pdf_value

# Example usage
alpha = [1.0, 2.0, 3.0]
x = [0.2, 0.5, 0.3]
pdf_value = dirichlet_pdf(alpha, x)
print(f"PDF value: {pdf_value}")
