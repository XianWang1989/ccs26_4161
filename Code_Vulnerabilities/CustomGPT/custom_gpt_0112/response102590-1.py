
import numpy as np
from scipy.special import gamma

def dirichlet_pdf(x, alpha):
    """
    Calculate the PDF of the Dirichlet distribution.

    Parameters:
    - x: array-like, shape (K,) where K is the number of parameters. 
         This should be a probability vector (i.e., sum(x) = 1).
    - alpha: array-like, shape (K,) the concentration parameters.

    Returns:
    - pdf: float, the probability density function evaluated at x.
    """
    if not (np.isclose(np.sum(x), 1) and np.all(x >= 0)):
        raise ValueError("x must be a probability vector (non-negative and sum to 1).")

    K = len(alpha)
    numerator = np.prod(x ** (alpha - 1))
    denominator = (gamma(np.sum(alpha)) /
                   np.prod(gamma(alpha)))

    pdf = numerator / denominator
    return pdf

# Example usage
alpha = [1, 1, 1]  # Uniform distribution over three categories
x = [0.2, 0.5, 0.3]  # Example probability vector
print("PDF:", dirichlet_pdf(x, alpha))
