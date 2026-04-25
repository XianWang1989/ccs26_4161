
import numpy as np
from scipy.integrate import odeint

# Parameters
a = 1
b = 5
tau = 3
num_components = 5

# Function to simulate your past data storage
class PastData:
    def __init__(self, size):
        self.past_values = np.zeros(size)
        self.index = 0

    def update(self, new_value):
        self.past_values[self.index] = new_value
        self.index = (self.index + 1) % len(self.past_values)

    def get(self, time_index):
        # return the value at a specific index if it's within the range
        if time_index < len(self.past_values):
            return self.past_values[time_index]
        else:
            return 0  # Return zero or another appropriate value for indices out of range

# Create an instance to hold past values
past_data = PastData(num_components)

# Differential equation system
def etaFunc(A, t):
    # Constants (example values)
    gamma = np.array([[0.5], [0.6], [0.7], [0.8], [0.9]])
    zeta = np.array([0.1] * num_components)
    tau = np.array([1.0, 1.0, 1.0, 1.0, 1.0])  # Your tau values
    theta = np.array([2, 3, 4, 5, 6])  # Example theta values

    # Update past values for the current time step
    past_data.update(A)

    # Compute the derivatives
    derivatives = np.zeros(num_components)

    for i in range(num_components):
        past_eta_value = past_data.get(int(t - theta[i]))  # Retrieve the past value
        derivatives[i] = (gamma[i] * past_eta_value - A[i] + zeta[i]) / tau[i]

    return derivatives

# Initial conditions and time span
initCond = np.zeros(num_components)  # Initial conditions
time = np.linspace(0, 10, 100)  # Time span

# Solve the differential equation
ETA = odeint(etaFunc, initCond, time)

# Extract results
eta_3 = ETA[:, 3]
print(eta_3)
