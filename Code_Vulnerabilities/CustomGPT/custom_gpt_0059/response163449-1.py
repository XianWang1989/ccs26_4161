
import numpy as np
from scipy.integrate import odeint

# Define constants
a = 1
b = 5
tau = 3

# Initialize past values
past_values = []

def eqtnSystem(Y, t):
    # Assuming past_values is a global variable
    global past_values

    # Update past values
    if len(past_values) < tau:
        past_values.append(Y.copy())  # Store current value
    else:
        past_values.pop(0)  # Remove oldest value
        past_values.append(Y.copy())  # Add current value

    # Calculate index for accessing past values
    idx = len(past_values) - tau

    # If we have enough history, calculate dY/dt
    if idx >= 0:
        dYdt = a * Y + b * past_values[idx]
    else:
        dYdt = a * Y  # No past value available yet

    return dYdt

# Initial conditions
initCond = [0]  # Example initial condition
time = np.linspace(0, 20, 100)  # Time points

# Solve the ODE
ETA = odeint(eqtnSystem, initCond, time)

# Access results
eta_0 = ETA[:, 0]
