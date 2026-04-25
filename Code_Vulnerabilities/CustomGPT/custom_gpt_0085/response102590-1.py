
import numpy as np
from scipy.special import gamma

def dirichlet_pdf(x, alpha):
    if np.sum(x) != 1 or np.any(x < 0):
        raise ValueError("Input probabilities must sum to 1 and be non-negative.")

    k = len(alpha)
    numerator = gamma(np.sum(alpha))
    denominator = np.prod(gamma(alpha))

    result = numerator / denominator * np.prod(x ** (alpha - 1))
    return result

# Example usage
alpha = np.array([2.0, 3.0, 5.0])
x = np.array([0.1, 0.3, 0.6])  # Must sum to 1

pdf_value = dirichlet_pdf(x, alpha)
print(f"PDF value: {pdf_value}")
