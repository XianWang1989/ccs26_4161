
import numpy as np
from scipy.integrate import odeint

# Define a class to manage the delayed values of eta
class DelayLine:
    def __init__(self, delay):
        self.delay = delay
        self.buffer = []

    def add(self, value):
        # Add the latest value, maintain buffer size
        self.buffer.append(value)
        if len(self.buffer) > self.delay:
            self.buffer.pop(0)

    def get(self, index):
        # Get the value from the buffer, if available
        if index < len(self.buffer):
            return self.buffer[-(index + 1)]  # Get the past value
        else:
            return 0  # Return 0 if no past value available

# ODE system with phase-shifted variable handling
def etaFunc(A, t, delay_line):
    # Unpack A (your current state vector)
    eta = A
    # Define constants
    gamma = np.array([[1]], dtype=float)
    beta = np.array([[0.5]], dtype=float)
    zeta = np.array([1])
    tau = np.array([1])  # Time constants
    theta = np.array([1])  # Phase shift timing

    # Store the current value for future delays
    delay_line.add(eta[0])

    # Define the differential equations with delay
    return np.array([
        (gamma[0, 0] * eta[0] - eta[0] + zeta[0]) / tau[0],
        (beta[0, 0] * delay_line.get(theta[0]) - eta[1] + zeta[1]) / tau[0]
    ])

# Initial conditions and parameters
initCond = np.array([0.0, 0.0])
time = np.linspace(0, 10, 100)

# Create a delay line for managing past values
delay_line = DelayLine(delay=3)

# Integrate the ODE
ETA = odeint(etaFunc, initCond, time, args=(delay_line,))

# Access results
eta_0 = ETA[:, 0]
eta_1 = ETA[:, 1]

# Print an example output
print("eta_0:", eta_0)
print("eta_1:", eta_1)
