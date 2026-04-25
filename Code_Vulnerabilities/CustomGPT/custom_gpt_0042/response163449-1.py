
import numpy as np
from scipy.integrate import odeint

# Parameters
a = 1.0
b = 5.0
tau = 3.0

# Time settings
time = np.linspace(0, 20, 200)  # Time vector
initCond = [1.0]  # Initial condition for the system

# Store past values
past_Y = []
past_steps = []

def eqtnSystem(Y, t):
    # Update the past values
    if len(past_Y) > 0:
        # Keep only values within the time range
        past_Y.append(Y[0])
        past_steps.append(t)
    else:
        past_Y.append(Y[0])
        past_steps.append(t)

    # Remove old values
    while past_steps and (t - past_steps[0] > tau):
        past_Y.pop(0)
        past_steps.pop(0)

    # Calculate Y(t - tau)
    if len(past_Y) > 1:  # Ensure we have enough past values
        Y_tau = past_Y[-2]  # Value at t - tau
    else:
        Y_tau = Y[0]  # Fallback, use current value

    # Return derivative
    return [a * Y[0] + b * Y_tau]

# Solve the differential equation
ETA = odeint(eqtnSystem, initCond, time)

# Example output
eta_0 = ETA[:, 0]
print(eta_0)
