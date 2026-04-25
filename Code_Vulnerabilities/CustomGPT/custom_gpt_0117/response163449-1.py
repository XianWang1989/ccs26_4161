
import numpy as np
from scipy.integrate import odeint
from scipy.interpolate import interp1d

# Define parameters
a = 1
b = 5
tau = 3

# Initialize history for eta
history = []

def etaFunc(A, t):
    global history
    # Update history with the new value
    history.append(A)

    # Interpolate past values, using max(t - tau) and corresponding index
    if len(history) > 1:
        # Create a time array
        time_points = np.linspace(0, len(history) - 1, len(history))
        interp_eta = interp1d(time_points, history, axis=0, fill_value="extrapolate")

        # Use interpolation to find eta at t - tau
        t_shifted = t - tau
        if t_shifted >= 0:
            Y_tau = interp_eta(np.interp(t_shifted, time_points, time_points))
        else:
            Y_tau = 0  # Handle case when tau is greater than the current time
    else:
        Y_tau = 0  # No history before first call

    return a * A + b * Y_tau

# Initial conditions and time setup
initCond = [1.0]
time = np.linspace(0, 20, 100)

# Perform integration
ETA = odeint(etaFunc, initCond, time)

# Access individual components of ETA
eta_0 = ETA[:, 0]
print(eta_0)
