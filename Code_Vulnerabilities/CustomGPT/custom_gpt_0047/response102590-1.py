
import numpy as np
from scipy.stats import dirichlet

# Parameters for the Dirichlet distribution
alpha = [1.0, 2.0, 3.0]  # This is the alpha parameter (concentration parameters)

# Sample points (x) where you want to evaluate the PDF
x = [0.2, 0.3, 0.5]  # Must sum to 1 and each value should be in [0, 1]

# Calculate the PDF
pdf_value = dirichlet.pdf(x, alpha)

print("The PDF of the Dirichlet distribution at {} is: {}".format(x, pdf_value))
