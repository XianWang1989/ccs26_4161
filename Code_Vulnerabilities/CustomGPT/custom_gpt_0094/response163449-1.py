
import numpy as np
from scipy.integrate import odeint

# Parameters
a = 1.0  # example constant
b = 5.0  # example constant
tau = 3.0  # time delay

# Create a history list to store past values
history = []

def etaFunc(A, t):
    global history

    # Ensure history is long enough to access past values
    while len(history) < int(t) + 1:
        history.append(0)  # Initialize past values with zero or another appropriate value

    current_value = A[0]

    # Store the current value for later access
    history[int(t)] = current_value

    # Use values from the history for delayed terms
    past_value = history[int(t - tau)] if t - tau >= 0 else 0  # Handle phase shift

    dYdt = a * current_value + b * past_value
    return [dYdt]

# Initial conditions
initCond = [0]  # You may set this according to your problem
time = np.linspace(0, 10, 100)  # Time vector

# Solve the differential equation
ETA = odeint(etaFunc, initCond, time)

# Example of accessing individual components
print(ETA[:, 0])
