
import numpy as np
from scipy.integrate import odeint

# Initial conditions and parameters
initCond = [0, 0, 0, 0, 0]
time = np.linspace(0, 20, 100)
theta = [1, 2, 3, 4, 5]  # Example phase shifts
tau = [1, 1, 1, 1, 1]  # Time constants
gamma = np.eye(5)  # Simplified for demonstration
beta = np.eye(5, 5)  # Simplified for demonstration
zeta = np.zeros(5)  # Steady-state input
eta = []

def pastEta(t, history, time_points):
    # Find the appropriate past value based on the time lag
    index = np.searchsorted(time_points, t) - 1
    return history[index] if index >= 0 else 0

def etaFunc(A, t, history, time_points):
    eta.append(A.copy())  # Store current state for future use
    return np.array([
        (gamma[0, 0] * xi(t - theta[0]) - A[0] + zeta[0]) / tau[0],
        (gamma[1, 1] * xi(t - theta[1]) - A[1] + zeta[1]) / tau[1],
        (gamma[2, 2] * xi(t - theta[2]) - A[2] + zeta[2]) / tau[2],
        (beta[3, 0] * pastEta(t - theta[3], history, time_points) +
         beta[3, 1] * pastEta(t - theta[4], history, time_points) +
         beta[3, 2] * pastEta(t - theta[5], history, time_points) - A[3] + zeta[3]) / tau[3],
        (beta[4, 3] * pastEta(t - theta[6], history, time_points) +
         beta[4, 2] * pastEta(t - theta[7], history, time_points) - A[4] + zeta[4]) / tau[4]
    ])

def xi(t):
    return np.array([np.sin(t), np.cos(t), 0])  # Example function

# Prepare to solve the ODE
history = []
eta = odeint(etaFunc, initCond, time, args=(history, time))

# Access the computed values
eta0 = eta[:, 0]
eta1 = eta[:, 1]
# ... and so on for other components

# Now you can work with the eta array as required
