
import numpy as np
from scipy.special import gamma

def dirichlet_pdf(alpha, x):
    if np.any(x < 0) or np.sum(x) != 1:
        raise ValueError("Input x must be a probability vector (non-negative and sum to 1).")
    return (np.prod(x ** (alpha - 1)) / (gamma(np.sum(alpha)) / np.prod(gamma(alpha))))

# Example usage
alpha = np.array([1.0, 2.0, 3.0])  # Concentration parameters
x = np.array([0.1, 0.2, 0.7])      # Probability vector

pdf_value = dirichlet_pdf(alpha, x)
print("PDF:", pdf_value)
