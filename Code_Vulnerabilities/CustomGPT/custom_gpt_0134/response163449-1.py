
import numpy as np
from scipy.integrate import odeint

# Constants
a = 1
b = 5
tau = 3.0  # Time delay

# Define the function for the ODE
def etaFunc(eta, t, past_values):
    # Update past values
    if len(past_values) >= int(tau):
        past_values.pop(0)  # Remove oldest value
    past_values.append(eta.copy())  # Store current value

    # Calculate the indices for previous values
    index_tau = max(len(past_values) - int(tau), 0)

    # Make sure to correctly reference past values
    past_eta = past_values[index_tau] if index_tau < len(past_values) else eta

    # Construct the system of equations
    d_eta = np.zeros_like(eta)
    d_eta[0] = a * eta[0] + b * past_eta[0]  # Example for first component
    # Repeat for other components as needed based on your system

    return d_eta

# Initial conditions
initCond = [0.0] * 5  # Adjust according to the number of components
time = np.linspace(0, 20, 100)  # Time vector

# History of eta values
past_values = []

# Integrate using odeint
ETA = odeint(etaFunc, initCond, time, args=(past_values,))

# Access individual components
eta_0 = ETA[:, 0]
eta_1 = ETA[:, 1]
# Add additional components as needed

# Use ETA for further analysis
