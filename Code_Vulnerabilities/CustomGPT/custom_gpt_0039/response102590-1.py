
import numpy as np
from scipy.special import gamma

def dirichlet_pdf(x, alpha):
    if np.sum(x) != 1 or np.any(x < 0):
        return 0  # Not in the simplex
    return (gamma(np.sum(alpha)) / np.prod(gamma(alpha))) * np.prod(x ** (alpha - 1))

# Example usage
alpha = np.array([2, 3, 5])  # Parameters for Dirichlet distribution
x = np.array([0.1, 0.2, 0.7])  # A point in the simplex

pdf_value = dirichlet_pdf(x, alpha)
print("PDF Value:", pdf_value)
