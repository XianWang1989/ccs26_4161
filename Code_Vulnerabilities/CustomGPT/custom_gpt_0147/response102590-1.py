
import numpy as np
from scipy.stats import dirichlet

# Step 1: Define the alpha parameters for the Dirichlet distribution
alpha = np.array([1.0, 2.0, 3.0])  # Example parameters

# Step 2: Create the Dirichlet distribution instance
distr = dirichlet(alpha)

# Step 3: Define a point in the simplex for which to calculate the PDF
point = np.array([0.2, 0.5, 0.3])  # Must sum to 1.0

# Step 4: Calculate the PDF at the definied point
pdf_value = distr.pdf(point)

# Step 5: Print the PDF value
print(f'The PDF value at point {point} is: {pdf_value}')
