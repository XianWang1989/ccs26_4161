
import numpy as np
from scipy.special import gammaln
from scipy.stats import dirichlet

def dirichlet_pdf(alpha, x):
    """
    Calculate the pdf of the Dirichlet distribution.

    Parameters:
        alpha (array-like): The concentration parameters (alpha).
        x (array-like): A point at which to evaluate the pdf.

    Returns:
        float: The pdf value at the point x.
    """
    # Calculate normalization constant
    normalization = gammaln(np.sum(alpha)) - np.sum(gammaln(alpha))

    pdf_value = np.exp(normalization + np.sum((alpha - 1) * np.log(x)))
    return pdf_value if np.all(x > 0) else 0.0

# Example usage:
alpha = [2, 5, 3]
x = [0.2, 0.5, 0.3]
print(f"PDF of Dirichlet distribution: {dirichlet_pdf(alpha, x)}")
