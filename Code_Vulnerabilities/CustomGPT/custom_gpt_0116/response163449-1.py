
import numpy as np
from scipy.integrate import odeint

# Parameters
a = 1
b = 5
tau = 3

# Global variable to store past states
history = []

def etaFunc(Y, t):
    # Global variable for history
    global history
    # Append current state to history
    history.append(Y.copy())

    # Retrieve the value from history based on time
    if len(history) > tau:
        Y_tau = history[-tau]  # This gets Y(t-tau)
    else:
        Y_tau = np.zeros_like(Y)  # Default if not enough past values

    # Differential equations
    dYdt = a * Y + b * Y_tau
    return dYdt

# Initial condition
initCond = np.array([0, 0, 0, 0, 0])  # Adjust as necessary
time = np.linspace(0, 30, 100)  # Time points for integration

# Clear history before integration
history = []
ETA = odeint(etaFunc, initCond, time)

# Example of extracting individual components
eta_0 = ETA[:, 0]

# Output the result for verification
print(eta_0)
