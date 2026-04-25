
import numpy as np
from scipy.special import gamma

def dirichlet_pdf(x, alpha):
    """
    Calculate the pdf of the Dirichlet distribution.

    Parameters:
    x (array-like): The input values (should sum to 1 and be in the range [0, 1]).
    alpha (array-like): The concentration parameters of the Dirichlet distribution.

    Returns:
    float: The probability density function value.
    """
    # Ensure input is a numpy array
    x = np.array(x)
    alpha = np.array(alpha)

    # Check if the length of alpha and x are the same
    if len(alpha) != len(x):
        raise ValueError("The dimensions of x and alpha must match.")

    # Check if x sums to 1
    if not np.isclose(np.sum(x), 1):
        raise ValueError("The input x must sum to 1.")

    # Calculate the numerator
    numerator = np.prod(x ** (alpha - 1))

    # Calculate the denominator
    denominator = np.prod(gamma(alpha)) / gamma(np.sum(alpha))

    # Return the pdf value
    return numerator / denominator

# Example usage
alpha_params = [2, 5, 3]  # Example concentration parameters
x_values = [0.2, 0.5, 0.3]  # Example input values (must sum to 1)

pdf_value = dirichlet_pdf(x_values, alpha_params)
print(f"The probability density function value is: {pdf_value}")
