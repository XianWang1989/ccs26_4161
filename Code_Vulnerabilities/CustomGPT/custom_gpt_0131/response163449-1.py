
import numpy as np
from scipy.integrate import odeint

# Define constants and parameters
a = 1
b = 5
tau = 3  # Delay time

# Function to handle past values with a buffer
class PastValues:
    def __init__(self, size):
        self.values = [0] * size
        self.index = 0

    def add(self, value):
        self.values[self.index] = value
        self.index = (self.index + 1) % len(self.values)

    def get(self, delay):
        """
        Get the past value for the given delay in time.
        The delay should be non-positive.
        """
        if delay >= 0:
            raise ValueError("Delay must be negative to access past values.")
        idx = (self.index + delay) % len(self.values)
        return self.values[idx]

# Initialize the buffer for past values
past_eta = PastValues(size=10)  # You can set an appropriate size

# Define the system of differential equations
def etaFunc(A, t):
    global past_eta  # Access the global past values storage
    # Assume gamma,eta,zeta,tau, and other constants are defined here
    # For example:
    beta = np.random.rand(5, 5)  # Replace with actual values
    theta = np.random.rand(5)     # Replace with actual values

    # Calculate current derivatives
    current_eta = A
    result = np.zeros_like(current_eta)

    result[0] = (a * current_eta[0] + b * past_eta.get(-int(tau))) / tau  # Example for eta_0
    past_eta.add(current_eta[0])  # Store current value

    # Similarly compute for other elements of the result
    # For instance, using `past_eta.get(-theta[i])` for accessing past values
    result[1] = ...  # Other equations use the same principle

    return result

# Initial conditions
initCond = [0, 0]  # Define appropriate initial conditions
time = np.linspace(0, 10, 100)  # Time vector

# Call integation
ETA = odeint(etaFunc, initCond, time)

# Extract components
eta_0 = ETA[:, 0]
eta_1 = ETA[:, 1]
