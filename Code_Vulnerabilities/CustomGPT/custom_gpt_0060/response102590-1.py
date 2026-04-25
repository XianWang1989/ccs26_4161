
import numpy as np
from scipy.special import gamma

def dirichlet_pdf(x, alpha):
    """Calculate the PDF of a Dirichlet distribution.

    Args:
        x (array-like): A vector of k probabilities that sum to 1 (0 < x_i < 1).
        alpha (array-like): The vector of concentration parameters.

    Returns:
        float: The value of the PDF at x.
    """
    # Ensure x is a numpy array
    x = np.asarray(x)
    alpha = np.asarray(alpha)

    # Check if the sum of x is close to 1 and all x's are positive
    if not np.all(x > 0) or not np.isclose(np.sum(x), 1):
        raise ValueError("x should be a vector of probabilities that sum to 1 and be greater than 0.")

    # Calculate the normalization constant B(alpha)
    B_alpha = np.prod(gamma(alpha)) / gamma(np.sum(alpha))

    # Calculate the numerator: product of x_i^{alpha_i - 1}
    numerator = np.prod(x**(alpha - 1))

    # Return the PDF value
    return numerator / B_alpha

# Example usage
alpha = [2.0, 3.0, 5.0]  # Concentration parameters
x = [0.1, 0.2, 0.7]      # A point in the simplex (should sum to 1)

pdf_value = dirichlet_pdf(x, alpha)
print(f"The PDF of the Dirichlet distribution at {x} is {pdf_value:.4f}")
