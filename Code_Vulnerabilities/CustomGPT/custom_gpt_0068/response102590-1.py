
import numpy as np
from scipy.special import gammaln

def dirichlet_pdf(x, alpha):
    """
    Calculate the pdf of the Dirichlet distribution.

    Parameters:
        x (array-like): A vector of probabilities (must sum to 1).
        alpha (array-like): The concentration parameters (must be positive).

    Returns:
        float: The value of the pdf at x.
    """
    if np.any(x < 0) or np.any(x > 1):
        return 0
    if not np.isclose(np.sum(x), 1):
        raise ValueError("The sum of the probabilities must be 1.")

    # Calculate the Dirichlet pdf
    return np.exp(np.sum(gammaln(alpha)) - gammaln(np.sum(alpha)) + 
                   np.sum((alpha - 1) * np.log(x)))

# Example usage
alpha = [1, 2, 3]  # concentration parameters
x = [0.2, 0.3, 0.5]  # probabilities (must sum to 1)

pdf_value = dirichlet_pdf(x, alpha)
print(f"The pdf of the Dirichlet distribution at {x} with alpha {alpha} is: {pdf_value}")
