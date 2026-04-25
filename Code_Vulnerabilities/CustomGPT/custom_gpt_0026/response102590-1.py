
import numpy as np
from scipy.special import gammaln

def dirichlet_pdf(alpha, x):
    """
    Calculate the PDF of the Dirichlet distribution.

    Parameters:
    alpha : array-like
        The concentration parameters of the Dirichlet distribution.
    x : array-like
        The points at which to compute the PDF, must sum to 1.

    Returns:
    float
        The calculated PDF value.
    """
    if not np.isclose(np.sum(x), 1):
        raise ValueError("The input x must sum to 1.")

    if any(x < 0):
        return 0  # PDF is 0 for negative x

    # Calculate the PDF using the Dirichlet formula
    a = gammaln(np.sum(alpha)) - np.sum(gammaln(alpha))
    b = np.sum((alpha - 1) * np.log(x))

    return np.exp(a + b)


# Example usage
alpha = [2, 5, 3]  # Concentration parameters
x = [0.2, 0.5, 0.3]  # Must sum to 1

pdf_value = dirichlet_pdf(alpha, x)
print("Dirichlet PDF value:", pdf_value)
