
import numpy as np
from scipy.integrate import odeint

# Parameters
a = 1
b = 5
tau = 3
time_steps = np.arange(0, 20, 0.1)  # Time array
initCond = [1]  # Initial condition

# Store past values
past_values = []

# Define the system of ODEs
def etaFunc(Y, t):
    global past_values

    # Interpolate past values
    if t - tau >= 0:
        # Get the index for past values
        past_Y = np.interp(t - tau, time_steps[:len(past_values)], past_values)
    else:
        past_Y = 0  # If outside range, assume zero contribution

    dYdt = a * Y + b * past_Y

    # Store current value
    past_values.append(Y[0])

    return [dYdt]

# Solve ODE
ETA = odeint(etaFunc, initCond, time_steps)

# Extract individual components
eta_0 = ETA[:, 0]

# Example output
print(eta_0)
