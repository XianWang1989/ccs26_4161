
import numpy as np
from scipy.special import gammaln

def dirichlet_pdf(x, alpha):
    if not np.isclose(np.sum(x), 1):
        raise ValueError("The sum of x must be 1.")
    if np.any(x < 0) or np.any(alpha <= 0):
        raise ValueError("All entries of x must be non-negative and alpha must be positive.")

    K = len(alpha)  # Number of categories
    log_pdf = (gammaln(np.sum(alpha)) 
                - np.sum(gammaln(alpha)) 
                + np.sum((alpha - 1) * np.log(x)))

    return np.exp(log_pdf)

# Example usage
alpha = np.array([1, 2, 3])  # Concentration parameters
x = np.array([0.1, 0.6, 0.3])  # Sample point (must sum to 1)
pdf_value = dirichlet_pdf(x, alpha)
print("PDF value:", pdf_value)
