
import numpy as np
from scipy.integrate import odeint

# Constants
gamma = np.array([[1, 2], [3, 4], [5, 6]])  # Example values
beta = np.array([[0.1, 0.2], [0.3, 0.4], [0.5, 0.6], [0.7, 0.8]])  # Example values
theta = np.array([1.0, 1.5, 2.0, 2.5, 3.0, 3.5])  # Example delays
tau = np.array([1, 1, 1, 1, 1])  # Example time constants

# Define initial conditions
initCond = np.zeros(5)  # Adjust based on your system

# Storage for past eta values
past_eta = []

def pastEta(t):
    # Find past eta values for times in the past
    return np.array([past for time, past in past_eta if time <= t])

def etaFunc(A, t):
    past_values = pastEta(t - theta)  # Gather past values
    past_eta.append((t, A.copy()))  # Store the current eta value

    # Calculate derivatives
    d_eta_dt = np.zeros_like(A)
    d_eta_dt[0] = (gamma[0, 0] * A[0] - A[0] + 0) / tau[0]  # Replace with proper zeta
    d_eta_dt[1] = (gamma[1, 1] * A[1] - A[1] + 0) / tau[1]  # Replace with proper zeta
    d_eta_dt[2] = (gamma[2, 2] * A[2] - A[2] + 0) / tau[2]  # Replace with proper zeta

    # Handle the non-instantaneous terms using past eta
    if len(past_values) > 0:
        d_eta_dt[3] = (beta[3, 0] * past_values[0] + beta[3, 1] * past_values[1] + 
                       beta[3, 2] * past_values[2] - A[3] + 0) / tau[3]
        d_eta_dt[4] = (beta[4, 3] * past_values[3] + beta[4, 2] * past_values[2] - A[4] + 0) / tau[4]

    return d_eta_dt

# Time points for integration
time = np.linspace(0, 10, 100)  # Adjust time range as needed

# Integrate using odeint
ETA = odeint(etaFunc, initCond, time)

# Access individual components
eta_0 = ETA[:, 0]
print(eta_0)
