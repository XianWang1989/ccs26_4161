
import numpy as np
from scipy.integrate import odeint

# Constants
a = 1
b = 5
tau = 3
time = np.linspace(0, 20, 200)  # Time array
initCond = [1, 0, 0, 0, 0]  # Initial conditions

# Store past values in a list
past_values = []

def past_eta(t, t_values, eta_values, tau):
    """Get the interpolated past eta value."""
    if t < 0:
        return 0  # Return 0 or another default if request is too far in the past
    for i in range(len(t_values)):
        if t >= t_values[i]:
            return eta_values[i]
    return 0

def etaFunc(A, t):
    """Defines the differential equations with phase shift."""
    # Keeps track of past time and values
    past_values.append((t, A.copy()))  # Store the current time and state

    # Prepare lists for interpolation
    t_values = np.array([pv[0] for pv in past_values])
    eta_values = np.array([pv[1] for pv in past_values])

    # Get the past eta values with phase shift
    past_eta_value = past_eta(t - tau, t_values, eta_values, tau)

    return np.array([
        a * A[0] + b * A[0],  # Example for unshifted
        a * A[1] + b * A[1],
        a * A[2] + b * A[2],
        (beta[3, 0] * past_eta_value + ...),  # Add other terms as necessary
        ...
    ])

# Usage of odeint
ETA = odeint(etaFunc, initCond, time)

# Retrieve specific components
eta_0 = ETA[:, 0]
