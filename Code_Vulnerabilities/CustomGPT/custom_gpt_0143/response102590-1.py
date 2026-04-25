
import numpy as np
from scipy.special import gamma

def dirichlet_pdf(x, alpha):
    # Ensure that x is a valid probability vector
    if np.sum(x) != 1 or np.any(x < 0):
        raise ValueError("x must be a valid probability vector (non-negative and sums to 1).")

    k = len(alpha)
    # Calculate the normalization constant
    normalization = np.prod(gamma(alpha)) / gamma(np.sum(alpha))

    # Calculate the PDF
    pdf = (1 / normalization) * np.prod(x ** (alpha - 1))
    return pdf

# Example usage
alpha = np.array([2, 3, 5])  # Concentration parameters
x = np.array([0.1, 0.3, 0.6])  # Sample point
pdf_value = dirichlet_pdf(x, alpha)
print("PDF value:", pdf_value)
