
import numpy as np
from scipy.integrate import odeint

# Constants
a = 1
b = 5
tau = 3

# Initialize an array to store past results
past_values = []

# Function to interpolate past values
def get_past_value(t, t_history, values):
    if t < 0 or len(t_history) == 0:
        return 0  # Return 0 if there's no valid past value
    # Find the index of the closest time in the history less than t
    idx = np.searchsorted(t_history, t) - 1
    if idx < 0:
        return 0  # No valid past values
    return values[idx]

# Define the system of equations
def etaFunc(A, t, t_history, past_values):
    # Store current time and current value
    t_history.append(t)
    past_values.append(A.copy())

    # Compute past values with phase shift
    Y_tau = get_past_value(t - tau, t_history, past_values)

    # Define the derivatives
    dYdt = a * A + b * Y_tau
    return dYdt

# Initial conditions
initCond = np.array([0])  # Adjust according to your system
time = np.linspace(0, 20, 100)  # Time vector for integration

# Initialize history lists
t_history = []
past_values = []

# Perform the integration
ETA = odeint(etaFunc, initCond, time, args=(t_history, past_values))

# Extract results
eta_0 = ETA[:, 0]

# Outputting results for inspection
print("ETA:", eta_0)
