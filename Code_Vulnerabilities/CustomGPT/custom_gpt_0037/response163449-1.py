
import numpy as np
from scipy.integrate import odeint

# Constants
a = 1
b = 5
tau = 3

# Storage for past values
past_values = []

def eqtnSystem(Y, t, past_values):
    Y_current = Y[0]

    # Get the shifted time value
    t_shifted = t - tau

    # Check for previous values
    Y_past = 0
    if past_values:
        # Use the latest past value if it's within valid range
        for time, value in reversed(past_values):
            if time <= t_shifted:
                Y_past = value
                break

    # Compute the derivative
    dYdt = a * Y_current + b * Y_past

    # Store current time and value
    past_values.append((t, Y_current))

    return [dYdt]

# Initial condition and time vector
init_cond = [0]  # Initial value of Y
time = np.linspace(0, 10, 100)  # Time array

# Integrate
ETA = odeint(eqtnSystem, init_cond, time, args=(past_values,))

# Access results
eta_0 = ETA[:, 0]

# Example output
print(eta_0)
