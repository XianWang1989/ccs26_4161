
import numpy as np
from scipy.special import gammaln

def dirichlet_pdf(alpha, x):
    if np.any(x < 0) or np.sum(x) != 1:
        return 0
    return np.exp(np.sum(gammaln(alpha)) - gammaln(np.sum(alpha)) + np.sum((alpha - 1) * np.log(x)))

# Example usage
alpha = np.array([1, 2, 3])  # Parameters of the Dirichlet distribution
x = np.array([0.1, 0.3, 0.6])  # A sample point
print(dirichlet_pdf(alpha, x))
