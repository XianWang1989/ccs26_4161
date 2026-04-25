
import numpy as np
from scipy.integrate import odeint

# Constants
a = 1
b = 5
tau = 3  # Delay

# Define time array
time = np.linspace(0, 30, 300)  # 30 seconds, 300 points
initCond = [1, 0, 0, 0, 0]  # Initial conditions for eta

# Store past values
past_values = []

# Function to get delayed value
def past_eta(t, past_values):
    if len(past_values) == 0:
        return [0, 0, 0]  # Zero if no past value available
    t_idx = np.searchsorted(time, t)  # Find index in the time array
    if t_idx > 0:
        return past_values[t_idx - 1]  # Get the last available value
    else:
        return [0, 0, 0]  # Default if out of range

# Function defining the system of equations
def etaFunc(A, t):
    # Append the current values to past_values
    if len(past_values) < len(time):
        past_values.append(A)

    # Calculate the values for eta using past values
    delayed_values = past_eta(t - tau, past_values)

    # Define your system of equations here
    return np.array([
        a * A[0] + b * delayed_values[0],
        # Add other components here as needed
    ])

# Integrate the system
ETA = odeint(etaFunc, initCond, time)

# Extract individual components
eta_0 = ETA[:, 0]
eta_1 = ETA[:, 1]
# and so on...
