
import numpy as np
from scipy.integrate import odeint

# Constants
a = 1
b = 5
tau = 3

# Initialize past values (for example, for 3 previous steps)
past_vals = []

def eqtnSystem(Y, t):
    global past_vals
    current_Y = Y[0]

    # Update past values list
    if len(past_vals) < tau:
        past_vals.append(current_Y)
    else:
        past_vals.pop(0)  # Remove oldest value
        past_vals.append(current_Y)

    # Retrieve Y(t-tau) if possible, else use the latest value
    Y_tau = past_vals[0] if len(past_vals) == tau else 0  # Or set to 0 if not available

    dYdt = a * current_Y + b * Y_tau
    return [dYdt]

# Time points
time = np.linspace(0, 10, 100)

# Initial condition
initCond = [0]

# Solve ODE
ETA = odeint(eqtnSystem, initCond, time)

# Access individual components
eta_0 = ETA[:, 0]

# Output
print(eta_0)
