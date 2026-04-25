
import numpy as np
from scipy.special import gamma

def dirichlet_pdf(x, alpha):
    if np.sum(x) != 1:
        raise ValueError("Input must sum to 1.")
    if np.any(x < 0):
        return 0  # PDF is 0 if any component is negative

    # Calculate the PDF
    numerator = np.prod(x**(alpha - 1))
    denominator = gamma(np.sum(alpha)) / np.prod(gamma(alpha))

    return numerator / denominator

# Example usage
alpha = np.array([1.0, 2.0, 3.0])  # Parameters of the Dirichlet distribution
x = np.array([0.2, 0.5, 0.3])  # Point to evaluate, must sum to 1

pdf_value = dirichlet_pdf(x, alpha)
print("PDF value:", pdf_value)
