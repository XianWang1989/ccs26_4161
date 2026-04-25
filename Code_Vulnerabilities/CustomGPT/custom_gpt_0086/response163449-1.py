
import numpy as np
from scipy.integrate import odeint

# Initialize constants and parameters
a = 1
b = 5
tau = 3
theta = [0, 1, 2, 3, 4, 5]  # Example phase shifts
initCond = [1, 0, 0, 0, 0]  # Initial conditions
time = np.linspace(0, 10, 100)  # Time points for integration
past_values = []

def etaFunc(A, t):
    # Unpack current state
    eta = A

    # Initialize current results array
    result = np.zeros_like(eta)

    # Store current value in past_values buffer
    past_values.append(eta.copy())

    # Limit the past_values to keep memory manageable, e.g., only keep tau time steps
    if len(past_values) > int(tau):
        past_values.pop(0)

    # Calculate dY/dt with phase shift
    # This assumes past_values has enough data points
    if t - tau >= 0 and len(past_values) > 0:
        past_eta = past_values[-1]  # Get the most recent past value

        result[0] = a * eta[0] + b * past_eta[0]  # Example for eta[0]
        result[1] = a * eta[1] + b * past_eta[1]  # Example for eta[1]
        # Continue for other components as needed...
    else:
        result = np.zeros_like(eta)  # Initial condition case

    return result

# Integrate using odeint
ETA = odeint(etaFunc, initCond, time)

# Accessing individual components
eta_0 = ETA[:, 0]
eta_1 = ETA[:, 1]
# Continue for other components...
