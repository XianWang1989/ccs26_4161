
import numpy as np
from scipy.integrate import odeint

# Parameters and constants setup
a = 1
b = 5
tau = 3
time = np.linspace(0, 20, 100)  # Time from 0 to 20 with 100 steps
initCond = [1, 1, 1, 1, 1]  # Initial conditions for eta

# To store past values, use a global or a shared structure
past_values = {}

def pastEta(t, y, t_prev):
    # Check if the previous time is in past_values
    if t in past_values:
        return past_values[t]
    else:
        # Interpolate or return a default value if not found
        return np.zeros(len(y))

def etaFunc(A, t):
    # Store the current time in the past_values for future access
    past_values[t] = A

    eta = A
    # Example constants (replace with your actual constants)
    gamma = np.diag([1, 1, 1])
    zeta = np.array([0, 0, 0, 0, 0])
    theta = np.array([1, 2, 3, 4, 5])

    # Use past values for computations
    eta3 = (beta[3, 0] * pastEta(t - theta[3], eta, time) \
           + beta[3, 1] * pastEta(t - theta[4], eta, time) \
           + beta[3, 2] * pastEta(t - theta[5], eta, time) \
           - eta[3] + zeta[3]) / tau

    eta4 = (beta[4, 3] * pastEta(t - theta[6], eta, time) \
           + beta[4, 2] * pastEta(t - theta[7], eta, time) \
           - eta[4] + zeta[4]) / tau

    # Returning the derivatives for all components
    return np.array([
        (gamma[0, 0] * eta[0] - eta[0] + zeta[0]) / tau,
        (gamma[1, 1] * eta[1] - eta[1] + zeta[1]) / tau,
        (gamma[2, 2] * eta[2] - eta[2] + zeta[2]) / tau,
        eta3,
        eta4
    ])

# Assuming beta is defined as a global or passed as needed
beta = np.random.rand(5, 5)  # Example beta matrix

# Integrating
ETA = odeint(etaFunc, initCond, time)
print(ETA[:, 0])  # Example to get eta_0
