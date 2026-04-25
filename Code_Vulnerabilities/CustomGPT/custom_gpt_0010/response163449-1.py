
import numpy as np
from scipy.integrate import odeint

# Initialize parameters
gamma = np.array([[1, 0], [0, 1], [1, 1]])
beta = np.array([[1, 1], [1, 1], [1, 1], [1, 1]])
zeta = [0, 0, 0, 0, 0]
tau = [1, 1, 1, 1, 1]
theta = [3, 3, 3, 3, 3]
initial_eta = [1, 1, 1, 0, 0]  # Initial conditions
time = np.linspace(0, 10, 100)

# Store past values for interpolation
eta_history = []

def pastEta(t, t_values, eta_values):
    # Simple linear interpolation for eta(t)
    if t < t_values[0]:
        return eta_values[0]  # Return first value if t is before the start
    for i in range(1, len(t_values)):
        if t_values[i] >= t:
            return eta_values[i - 1] + (eta_values[i] - eta_values[i - 1]) * (t - t_values[i - 1]) / (t_values[i] - t_values[i - 1])
    return eta_values[-1]  # Return last value if t exceeds available data

def etaFunc(A, t):
    global eta_history
    eta_history.append(A.copy())  # Store the current value of eta
    past_time_values = np.linspace(0, t, len(eta_history))
    past_eta_values = np.array(eta_history)

    return np.array([
        (gamma[0, 0] * xi(t - theta[0]) - A[0] + zeta[0]) / tau[0],
        (gamma[1, 1] * xi(t - theta[1]) - A[1] + zeta[1]) / tau[1],
        (gamma[2, 2] * xi(t - theta[2]) - A[2] + zeta[2]) / tau[2],
        (beta[3, 0] * pastEta(t - theta[3], past_time_values, past_eta_values[:,3]) + 
         beta[3, 1] * pastEta(t - theta[4], past_time_values, past_eta_values[:,4]) - 
         A[3] + zeta[3]) / tau[3],
        (beta[4, 3] * pastEta(t - theta[6], past_time_values, past_eta_values[:,3]) +
         beta[4, 2] * pastEta(t - theta[7], past_time_values, past_eta_values[:,2]) - 
         A[4] + zeta[4]) / tau[4]
    ])

# Define xi function
def xi(t):
    return np.sin(t)  # Example function, replace with your actual function

# Integrate using odeint
ETA = odeint(etaFunc, initial_eta, time)

# Access individual components
eta_0 = ETA[:, 0]
print(eta_0)
