
import numpy as np
from scipy import integrate

# Example constants
a = 1
b = 5
tau = 3

# This will store the history of eta values
eta_history = []

# Define the function to find past eta values
def pastEta(t):
    # Return the last eta values if available and t corresponds to previous time
    if len(eta_history) == 0 or t < 0:
        return np.array([0, 0, 0])  # Default values if no history available
    # Get the last calculated value corresponding to t
    if len(eta_history) * dt + start_time >= t:
        idx = int((t - start_time) // dt)  # Finding the index
        return eta_history[idx]  # Return the historic eta value
    else:
        return np.array([0, 0, 0])  # Default if out of bounds

# The differential equation function with phase shift
def etaFunc(A, t):
    # Assuming you have defined constants like gamma, theta, beta, zeta
    new_eta = np.zeros_like(A)

    new_eta[0] = (gamma[0, 0] * xi(t - theta[0])[0] - A[0] + zeta[0]) / tau[0]
    new_eta[1] = (gamma[1, 1] * xi(t - theta[1])[1] - A[1] + zeta[1]) / tau[1]
    new_eta[2] = (gamma[2, 2] * xi(t - theta[2])[2] - A[2] + zeta[2]) / tau[2]

    # Utilizing pastEta for the phase-shifted components
    past_values = pastEta(t - theta[3])
    new_eta[3] = (beta[3, 0]*past_values[0] + beta[3, 1]*past_values[1] + beta[3, 2]*past_values[2] - A[3] + zeta[3]) / tau[3]

    past_values = pastEta(t - theta[4])
    new_eta[4] = (beta[4, 3]*past_values[3] + beta[4, 2]*past_values[2] - A[4] + zeta[4]) / tau[4]

    # Save the new eta in history
    eta_history.append(new_eta)

    return new_eta

# Initialization parameters
initCond = np.array([1, 1, 1, 0, 0])  # Initial conditions for your system
time = np.linspace(0, 10, 100)  # Time points

# Assuming you define start_time and dt for backward indexing
start_time = time[0]
dt = time[1] - time[0]

# Solving the differential equations
ETA = integrate.odeint(etaFunc, initCond, time)

# Access components of ETA
eta_0 = ETA[:, 0]
eta_1 = ETA[:, 1]
