
import numpy as np
from scipy.special import gammaln

def dirichlet_pdf(alpha, x):
    """
    Calculate the PDF of the Dirichlet distribution.

    Parameters:
    - alpha: array-like, the concentration parameters (length k)
    - x: array-like, the probabilities (length k) such that sum(x) = 1

    Returns:
    - PDF value
    """
    # Ensure the input is a numpy array
    x = np.asarray(x)

    # Check if x is valid and sums to 1
    if not np.allclose(np.sum(x), 1):
        raise ValueError("x must sum to 1.")

    k = len(alpha)

    # Compute the PDF
    return (np.prod(x ** (alpha - 1)) / 
            np.exp(gammaln(np.sum(alpha)) - np.sum(gammaln(alpha))))

# Example usage
alpha = [1.0, 2.0, 3.0]  # Concentration parameters
x = [0.1, 0.5, 0.4]      # Probabilities (must sum to 1)

pdf_value = dirichlet_pdf(alpha, x)
print("PDF value:", pdf_value)
