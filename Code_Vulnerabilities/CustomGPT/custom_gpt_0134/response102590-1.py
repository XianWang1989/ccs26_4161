
import numpy as np
from scipy.special import gamma
from numpy import prod

def dirichlet_pdf(x, alpha):
    # Ensure that x sums up to 1
    if not np.isclose(np.sum(x), 1):
        raise ValueError("x must sum to 1")

    # Calculate the PDF
    numerator = prod(x ** (alpha - 1))
    denominator = gamma(np.sum(alpha)) / prod(gamma(alpha))

    return numerator / denominator

# Example usage
alpha = np.array([1.0, 2.0, 3.0])  # Parameters of the Dirichlet distribution
x = np.array([0.2, 0.5, 0.3])       # Point at which to evaluate the PDF

pdf_value = dirichlet_pdf(x, alpha)
print(f"PDF value: {pdf_value}")
