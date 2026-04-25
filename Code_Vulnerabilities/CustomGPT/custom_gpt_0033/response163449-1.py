
import numpy as np
from scipy.integrate import odeint

# Parameters
a = 1
b = 5
tau = 3

# Initialization
initCond = [0]  # Example initial condition
time = np.linspace(0, 10, 100)  # Time range

# Store past eta values
past_eta = []  # History of eta values

def etaFunc(Y, t):
    # Update past_eta list
    if len(past_eta) > 0:
        Y_tau = past_eta[-1] if t - tau >= 0 else 0  # Use last value if enough time has passed
    else:
        Y_tau = 0  # Initial value if this is the first call

    # Calculate current rate of change
    dYdt = a * Y + b * Y_tau

    # Append current Y for future references
    past_eta.append(Y)

    return dYdt

# Run the integration
ETA = odeint(etaFunc, initCond, time)

# Extract individual components
eta_0 = ETA[:, 0]

# Example output
print(eta_0)
