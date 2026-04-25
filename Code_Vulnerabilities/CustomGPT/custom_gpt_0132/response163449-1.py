
import numpy as np
from scipy.integrate import odeint

# Constants
gamma = np.array([[1], [2], [3]])  # Replace with your actual constants
theta = [1, 2, 3, 4, 5, 6, 7]  # Sample constants
zeta = np.zeros(4)  # Replace with your zeta values
tau = [1, 1, 1, 1, 1]  # Sample tau values
beta = np.random.rand(5, 5)  # Random beta for illustration

# Storage for past eta values
past_eta_values = []

def pastEta(t, time_series, eta_series):
    # Get the index of the time point just before t
    idx = np.searchsorted(time_series, t) - 1
    if idx >= 0:
        return eta_series[idx]
    else:
        return 0  # Or some appropriate default which signifies no past value

def etaFunc(A, t):
    global past_eta_values  # To access the list of past eta values

    # Store current eta value
    past_eta_values.append(A.copy())

    # Current time series and values
    time_series = np.linspace(0, t, len(past_eta_values))

    # Calculate past values with interpolation
    eta_3 = (beta[3, 0] * pastEta(t - theta[3], time_series, past_eta_values) +
              beta[3, 1] * pastEta(t - theta[4], time_series, past_eta_values) +
              beta[3, 2] * pastEta(t - theta[5], time_series, past_eta_values) -
              A[3] + zeta[3]) / tau[3]

    eta_4 = (beta[4, 3] * pastEta(t - theta[6], time_series, past_eta_values) +
              beta[4, 2] * pastEta(t - theta[7], time_series, past_eta_values) -
              A[4] + zeta[4]) / tau[4]

    return np.array([
        (gamma[0, 0] * 1 - A[0] + zeta[0]) / tau[0],
        (gamma[1, 1] * 2 - A[1] + zeta[1]) / tau[1],
        (gamma[2, 2] * 3 - A[2] + zeta[2]) / tau[2],
        eta_3,
        eta_4
    ])

# Initial conditions and time points
initCond = np.zeros(5)  # Replace with actual initial conditions
time = np.linspace(0, 20, 100)  # Time points for integration

# Integrate the system
ETA = odeint(etaFunc, initCond, time)

# Access individual components
eta_0 = ETA[:, 0]
eta_1 = ETA[:, 1]
# and so forth...

# Reset past values for a new integration scenario
past_eta_values = []
