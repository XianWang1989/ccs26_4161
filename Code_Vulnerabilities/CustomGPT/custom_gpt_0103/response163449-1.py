
import numpy as np
from scipy.integrate import odeint

# Constants
a = 1
b = 5
tau = 3
time_steps = 100
time = np.linspace(0, 20, time_steps)

# Function to compute past values
def past_eta(t, eta_vals, timestamps, tau):
    # Find the index for the closest past value
    idx = np.searchsorted(timestamps, t - tau)
    if idx == 0:
        return 0  # Or handle boundary condition however required
    return eta_vals[idx - 1]

# Differential equation system
def etaFunc(eta, t, timestamps):
    # Calculate Y(t) and Y(t-tau)
    current_eta = eta[0]
    past_eta_value = past_eta(t, eta_values, timestamps, tau)

    dYdt = a * current_eta + b * past_eta_value
    return [dYdt]

# Initial condition
initCond = [0]  # Example initial condition
eta_values = np.zeros((time_steps, len(initCond)))  # To store computed values
timestamps = []

# Integration loop
for i in range(time_steps):
    if i == 0:
        timestamps.append(time[i])
        eta_values[i] = initCond
        continue
    t = time[i]
    eta_current = eta_values[i - 1]

    # Get the next value using odeint
    new_eta = odeint(etaFunc, eta_current, [t], args=(timestamps,))
    eta_values[i] = new_eta[0]
    timestamps.append(t)

# Extract results
eta_0 = eta_values[:, 0]

# Example output
print("Results for eta_0:", eta_0)
