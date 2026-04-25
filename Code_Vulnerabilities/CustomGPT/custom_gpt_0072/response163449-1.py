
import numpy as np
from scipy.integrate import odeint

# Define the parameters
a = 1
b = 5
tau = 3

# Initialize a history list for past values
history = []

def eqtnSystem(Y, t):
    # Store the current Y in history (for past values)
    history.append(Y)

    # Get the past value at t-tau if history is long enough
    if len(history) > tau:
        Y_past = history[-tau]  # Corresponds to Y(t-tau)
    else:
        Y_past = 0  # Use zero or another suitable initial condition

    # Define the equation
    dYdt = a * Y + b * Y_past
    return dYdt

# Define initial conditions and time vector
initCond = [0]  # Change as needed
time = np.linspace(0, 20, 100)

# Perform integration
Y = odeint(eqtnSystem, initCond, time)

# Extract and print results
print(Y[:, 0])
