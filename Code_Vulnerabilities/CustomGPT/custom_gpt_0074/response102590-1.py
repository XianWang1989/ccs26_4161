
import numpy as np
from scipy.stats import dirichlet

# Parameters for the Dirichlet distribution (alpha)
alpha = [2.0, 5.0, 3.0]

# Points at which to evaluate the pdf
x = [0.2, 0.5, 0.3]

# Check if the points sum to 1 (valid for Dirichlet distribution)
if np.isclose(sum(x), 1):
    # Calculate the pdf
    pdf_value = dirichlet.pdf(x, alpha)
    print(f'The pdf value at {x} for the Dirichlet distribution with alpha {alpha} is: {pdf_value}')
else:
    print("The input probabilities must sum to 1.")
