
import numpy as np
from scipy.integrate import odeint

# Define the function to hold past values of eta
class PastValues:
    def __init__(self, size):
        self.values = np.zeros(size)
        self.index = 0

    def update(self, new_value):
        self.values[self.index] = new_value
        self.index = (self.index + 1) % self.values.size

    def get(self, t_shift):
        # Return the appropriate past value based on the shift
        index = (self.index - int(t_shift)) % self.values.size
        return self.values[index]

# Initialize constants
tau = 3
num_components = 5
past_eta = PastValues(num_components)

def etaFunc(A, t):
    a = 1
    b = 5
    # Update past values with current eta
    past_eta.update(A)

    # Compute the current derivatives
    dYdt = np.zeros(num_components)
    dYdt[0] = a * A[0] + b * past_eta.get(tau)  # Use past value for t-tau
    # Example for other components (modify as needed)
    for i in range(1, num_components):
        dYdt[i] = (gamma[i,i] * xi(t - theta[i])[i] - eta[i] + zeta[i]) / tau[i]

    return dYdt

# Initial conditions and time
initCond = np.random.rand(num_components)  # Example initial condition
time = np.linspace(0, 10, 100)  # Time span

# Integrated results
ETA = odeint(etaFunc, initCond, time)

# Access each component
eta_0 = ETA[:, 0]
