
import numpy as np
from scipy.special import gammaln

def dirichlet_pdf(alpha, x):
    if np.any(x < 0) or np.sum(x) != 1:
        return 0
    return np.exp(np.sum(gammaln(alpha)) - gammaln(np.sum(alpha)) + np.sum((alpha - 1) * np.log(x)))

# Example usage
alpha = np.array([2.0, 3.0, 5.0])  # Dirichlet parameters
x = np.array([0.1, 0.2, 0.7])       # Point at which to evaluate PDF

pdf_value = dirichlet_pdf(alpha, x)
print(f"PDF value: {pdf_value}")
