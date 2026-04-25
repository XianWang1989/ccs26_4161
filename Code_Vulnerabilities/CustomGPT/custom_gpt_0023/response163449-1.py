
import numpy as np
from scipy.integrate import odeint

# Parameters
a = 1
b = 5
tau = 3

# Time configuration
time_points = np.linspace(0, 10, 100)  # Time from 0 to 10

# Function to calculate the derivatives
def eqtnSystem(Y, t, past_Y):
    # Get the current value and the past value if available
    current_Y = Y[0]
    past_Y_val = past_Y(t) if t > tau else 0  # Assuming 0 for undefined history
    dYdt = a * current_Y + b * past_Y_val
    return [dYdt]

# History tracking function
def get_past_Y(history, t):
    # Return the appropriate past value based on t
    if t < 0 or len(history) == 0:
        return 0  # No history available
    # Find the latest previous value
    return history[max(0, np.searchsorted(history_times, t) - 1)]

# Initialize variables
init_cond = [1]  # Initial condition
history = []
history_times = []

# Define a wrapper for the integration to maintain history
def integrate_system():
    global history, history_times

    def track_history(t, Y):
        history.append(Y[0])
        history_times.append(t)

    # Integration
    results = odeint(eqtnSystem, init_cond, time_points, args=(get_past_Y,))

    # Track history after calculation
    for t, Y in zip(time_points, results):
        track_history(t, Y)

    return results

# Integrate and get the results
ETA = integrate_system()

# Access results
eta_0 = ETA[:, 0]
print(eta_0)
