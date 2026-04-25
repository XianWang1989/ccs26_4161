
import numpy as np
from scipy.integrate import odeint

# Define the global list to store past values
past_eta_values = []

def pastEta(t):
    """
    This function returns the past value of eta at time t.
    If t is not available, it returns 0 or some default value.
    """
    global past_eta_values
    # Check if we have stored past values
    if len(past_eta_values) > 0:
        # Find the index of the nearest past value (as an example, can be tailored)
        indices = np.array([i[0] for i in enumerate(past_eta_values)])
        index = np.argmin(np.abs(indices - t))
        return past_eta_values[index][1] if index < len(past_eta_values) else 0
    return 0

def etaFunc(A, t):
    global past_eta_values
    # Store A (eta current values) in the list of past values
    past_eta_values.append((t, A.copy()))

    # Example parameters
    gamma = np.array([[1, 0], [0, 1], [1, 1]])
    zeta = np.array([1, 1, 1, 1, 1])
    tau = np.array([1, 1, 1, 1, 1])
    beta = np.zeros((5, 5))

    # Extract current eta values
    eta = A

    # Your differential function with phase shifts
    return np.array([
        (gamma[0, 0] * 1 - eta[0] + zeta[0]) / tau[0],
        (gamma[1, 1] * 1 - eta[1] + zeta[1]) / tau[1],
        (gamma[2, 2] * 1 - eta[2] + zeta[2]) / tau[2],
        (beta[3, 0] * pastEta(t - 1) + beta[3, 1] * pastEta(t - 2) - eta[3] + zeta[3]) / tau[3],
        (beta[4, 3] * pastEta(t - 1) + beta[4, 2] * pastEta(t - 2) - eta[4] + zeta[4]) / tau[4]
    ])

# Initial conditions and time points
initCond = [1, 0, 0, 0, 0]  # Initial values for eta
time = np.linspace(0, 10, 100)  # Time array

# Integrate the system over time
ETA = odeint(etaFunc, initCond, time)

# Access specific components of ETA
eta_0 = ETA[:, 0]
