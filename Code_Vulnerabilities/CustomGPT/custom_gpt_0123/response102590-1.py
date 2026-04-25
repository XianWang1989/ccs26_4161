
import numpy as np
from scipy.special import gamma

def dirichlet_pdf(alpha, x):
    """
    Calculate the PDF of the Dirichlet distribution.

    Parameters:
    alpha : array_like
        The parameter of the Dirichlet distribution (must be positive).
    x : array_like
        The input values (must be in the simplex, i.e., sum(x) = 1 and all x >= 0).

    Returns:
    float
        The value of the PDF at x.
    """
    if not np.all(alpha > 0):
        raise ValueError("All parameters in alpha must be positive.")
    if not np.isclose(np.sum(x), 1) or np.any(x < 0):
        raise ValueError("x must be in the simplex (sum(x) = 1 and all x >= 0).")

    numerator = np.prod(x ** (alpha - 1))
    denominator = np.prod(gamma(alpha)) / gamma(np.sum(alpha))

    return numerator / denominator

# Example usage
alpha = [2.0, 5.0, 3.0]  # Dirichlet parameters
x = [0.1, 0.3, 0.6]      # Sample point in the simplex
pdf_value = dirichlet_pdf(alpha, x)

print(f"The PDF value of the Dirichlet distribution at x={x} is {pdf_value:.4f}")
