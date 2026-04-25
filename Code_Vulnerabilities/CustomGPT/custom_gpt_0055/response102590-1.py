
import numpy as np
from scipy.special import gammaln

def dirichlet_pdf(x, alpha):
    if np.any(x < 0) or np.sum(x) != 1:
        raise ValueError("x must be non-negative and sum to 1")

    # Calculate the PDF
    normalization = np.exp(gammaln(np.sum(alpha)) - np.sum(gammaln(alpha)))
    return normalization * np.prod(x**(alpha - 1))

# Example usage
alpha = np.array([1, 2, 3])
x = np.array([0.1, 0.6, 0.3])  # should sum to 1
pdf_value = dirichlet_pdf(x, alpha)
print("PDF value:", pdf_value)
