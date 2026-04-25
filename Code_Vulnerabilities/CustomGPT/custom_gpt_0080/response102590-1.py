
import numpy as np
from scipy.special import gamma

def dirichlet_pdf(alpha, x):
    """
    Calculate the PDF of the Dirichlet distribution.

    Parameters:
    alpha : array-like
        Concentration parameters of the Dirichlet distribution.
    x : array-like
        Input points where the PDF is evaluated (must sum to 1 and be in [0, 1]).

    Returns:
    float
        The value of the PDF at x.
    """
    if not np.isclose(np.sum(x), 1) or np.any(x < 0) or np.any(x > 1):
        raise ValueError("x must sum to 1 and be in the interval [0, 1].")

    numerator = np.prod([gamma(a) for a in alpha])
    denominator = gamma(np.sum(alpha))
    pdf_value = (np.prod(x ** (alpha - 1)) * numerator) / denominator
    return pdf_value

# Example usage
alpha = [1.0, 2.0, 3.0]  # Concentration parameters
x = [0.2, 0.5, 0.3]      # Points where PDF is evaluated

pdf_value = dirichlet_pdf(alpha, x)
print(f"PDF value: {pdf_value}")
