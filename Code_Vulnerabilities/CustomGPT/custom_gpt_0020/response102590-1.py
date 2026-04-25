
import numpy as np
from scipy.stats import dirichlet

# Parameters of the Dirichlet distribution
alpha = [1.0, 2.0, 3.0]  # Concentration parameters
# Make sure that alpha sums to greater than zero and has length equal to the output
if sum(alpha) <= 0 or len(alpha) == 0:
    raise ValueError("Alpha parameters must be positive and non-empty.")

# A point at which to evaluate the pdf
x = [0.2, 0.3, 0.5]  # Make sure the sum of x is 1 and each element is between 0 and 1
if not (np.isclose(sum(x), 1.0) and all(0 <= xi <= 1 for xi in x)):
    raise ValueError("x must be a valid probability vector that sums to 1.")

# Calculate the pdf
pdf_value = dirichlet.pdf(x, alpha)

print(f"The pdf of the Dirichlet distribution at {x} is: {pdf_value}")
