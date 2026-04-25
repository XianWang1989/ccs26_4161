
import numpy as np
from scipy.special import gamma

def dirichlet_pdf(alpha, x):
    """
    Calculate the pdf of the Dirichlet distribution.

    Parameters:
        alpha (array-like): Concentration parameters (greater than 0).
        x (array-like): Input probabilities (must sum to 1 and be in the range [0, 1]).

    Returns:
        float: The pdf value at x.
    """

    # Check if the input probabilities sum to 1
    if not np.isclose(np.sum(x), 1):
        raise ValueError("Input probabilities must sum to 1.")

    # Calculate the pdf using the formula
    numerator = np.prod(x ** (alpha - 1))
    denominator = gamma(np.sum(alpha)) / np.prod(gamma(alpha))

    return numerator / denominator

# Example usage
alpha = [2, 3, 5]  # Concentration parameters
x = [0.1, 0.2, 0.7]  # Input probabilities

pdf_value = dirichlet_pdf(alpha, x)
print("The pdf of the Dirichlet distribution at x is:", pdf_value)
