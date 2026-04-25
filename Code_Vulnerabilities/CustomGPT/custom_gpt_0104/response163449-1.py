
import numpy as np
from scipy import integrate

# Constants (replace with your actual values)
gamma = np.array([[...], [...], [...]])
beta = np.array([[...], [...]])
zeta = np.array([...])
tau = np.array([...])
theta = np.array([...])
initCond = np.array([...])  # Initial conditions
time = np.linspace(0, 10, 100)  # Time points

# To store historical eta values
eta_history = []

def pastEta(t_minus_theta, t_history, eta_history):
    """
    Function to retrieve past values of eta based on the shifted time.
    """
    if t_minus_theta < 0 or len(eta_history) == 0:
        return np.zeros_like(eta_history[0])  # Returns zeros if no past value exists
    t_index = np.searchsorted(t_history, t_minus_theta) - 1
    if t_index >= 0:
        return eta_history[t_index]
    else:
        return np.zeros_like(eta_history[0])  # Default return for out of range

def etaFunc(A, t):
    # Store eta in history
    eta_history.append(A)
    t_history = np.linspace(0, t, len(eta_history) + 1)  # Create time history array

    # Calculate the derivatives according to your equation
    result = np.array([
        (gamma[0,0] * xi(t - theta[0])[0] - A[0] + zeta[0]) / tau[0],
        (gamma[1,1] * xi(t - theta[1])[1] - A[1] + zeta[1]) / tau[1],
        (gamma[2,2] * xi(t - theta[2])[2] - A[2] + zeta[2]) / tau[2],
        (beta[3,0] * pastEta(t - theta[3], t_history, eta_history)[0] +
         beta[3,1] * pastEta(t - theta[4], t_history, eta_history)[1] +
         beta[3,2] * pastEta(t - theta[5], t_history, eta_history)[2] - A[3] + zeta[3]) / tau[3],
        (beta[4,3] * pastEta(t - theta[6], t_history, eta_history)[3] +
         beta[4,2] * pastEta(t - theta[7], t_history, eta_history)[2] - A[4] + zeta[4]) / tau[4]
    ])
    return result

# Integrate the system
ETA = integrate.odeint(etaFunc, initCond, time)

# Accessing individual components of ETA
eta_0 = ETA[:, 0]
eta_1 = ETA[:, 1]
# and so on...
