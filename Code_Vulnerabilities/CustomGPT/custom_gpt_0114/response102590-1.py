
import numpy as np
from scipy.special import gammaln
from scipy.stats import dirichlet

def dirichlet_pdf(alpha, x):
    if np.any(x < 0) or np.sum(x) != 1:
        return 0  # Invalid because x must be a probability vector
    return (np.prod(x**(alpha - 1)) / np.exp(gammaln(np.sum(alpha)) - np.sum(gammaln(alpha))))

# Parameters for the Dirichlet distribution
alpha = np.array([1, 2, 3])
# Example probability vector
x = np.array([0.1, 0.5, 0.4])

# Calculate the pdf
pdf_value = dirichlet_pdf(alpha, x)
print(f"PDF value: {pdf_value}")
