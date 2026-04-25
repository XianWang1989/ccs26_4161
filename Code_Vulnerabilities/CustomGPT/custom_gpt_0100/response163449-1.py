
import numpy as np
from scipy.integrate import odeint

# Parameters
a = 1.0
b = 5.0
tau = 3.0
time = np.linspace(0, 10, 100)  # Time array
initCond = [1]  # Initial condition

# Function to store previous values
class PastValues:
    def __init__(self, tau):
        self.tau = tau
        self.history = []

    def add(self, value):
        self.history.append(value)
        # Keep only values within the time window
        if len(self.history) > self.tau:
            self.history.pop(0)

    def get(self, t):
        # Return the last value before t, based on tau
        if len(self.history) == 0 or t < 0:
            return 0  # No past value, return zero
        return self.history[max(0, len(self.history) - 1 - self.tau)]

past_values = PastValues(tau)

def eqtnSystem(Y, t):
    # Store the current value
    past_values.add(Y[0])
    # Calculate the delayed value
    Y_delayed = past_values.get(t - tau)

    # Define the equation
    dYdt = a * Y[0] + b * Y_delayed
    return [dYdt]

# Integrate the system
ETA = odeint(eqtnSystem, initCond, time)

# Access individual components
eta_0 = ETA[:, 0]

# For plotting or further processing
import matplotlib.pyplot as plt
plt.plot(time, eta_0)
plt.xlabel('Time')
plt.ylabel('eta_0')
plt.title('Response of the system')
plt.grid()
plt.show()
