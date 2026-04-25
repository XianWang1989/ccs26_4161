
import numpy as np
from scipy.special import gammaln

def dirichlet_pdf(x, alpha):
    # Validate input
    if not (np.all(x >= 0) and np.isclose(np.sum(x), 1)):
        raise ValueError("x must be a valid probability vector summing to 1.")

    # Calculate the PDF
    log_pdf = (gammaln(np.sum(alpha)) - np.sum(gammaln(alpha)) +
                np.sum((alpha - 1) * np.log(x)))

    return np.exp(log_pdf)

# Example usage
alpha = np.array([1.0, 2.0, 3.0])
x = np.array([0.2, 0.5, 0.3])
pdf_value = dirichlet_pdf(x, alpha)
print("PDF Value:", pdf_value)
