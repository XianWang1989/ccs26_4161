
import numpy as np
from scipy.special import gamma

def dirichlet_pdf(x, alpha):
    # Ensure x is a numpy array and non-negative
    x = np.asarray(x)
    if np.any(x < 0) or not np.isclose(np.sum(x), 1):
        raise ValueError("x must be a positive vector that sums to 1")

    # Calculate the multivariate beta function normalization
    B_alpha = np.prod(gamma(alpha)) / gamma(np.sum(alpha))

    # Calculate the pdf
    pdf = (np.prod(x ** (alpha - 1))) / B_alpha
    return pdf

# Example usage
alpha = [2, 5, 3]  # parameters of the Dirichlet distribution
x = [0.1, 0.3, 0.6]  # point at which to evaluate the pdf

pdf_value = dirichlet_pdf(x, alpha)
print(f"The pdf value of the Dirichlet distribution at x = {x} with alpha = {alpha} is: {pdf_value}")
