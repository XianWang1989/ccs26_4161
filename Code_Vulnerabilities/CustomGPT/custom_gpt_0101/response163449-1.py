
import numpy as np
from scipy.integrate import odeint

# Constants
a = 1
b = 5
tau = 3

# Parameters for the eta function
gamma = np.array([[...]])  # Define your gamma array
eta = np.zeros(5)  # Example initialization
zeta = np.zeros(5)  # Example initialization
theta = np.array([...])  # Define your theta array
beta = np.array([[...], [...], [...], [...]])  # Define beta array
past_values = []  # To store past computed values

def pastEta(t):
    # Retrieve past values based on time
    return np.array([value for time, value in past_values if time < t])

def etaFunc(A, t):
    global past_values
    # Store the current time and computed values
    past_values.append((t, A))

    # Calculate eta based on the current state A
    return np.array([(gamma[0, 0] * xi(t - theta[0]) - eta[0] + zeta[0]) / tau[0],
                     (gamma[1, 1] * xi(t - theta[1]) - eta[1] + zeta[1]) / tau[1],
                     (gamma[2, 2] * xi(t - theta[2]) - eta[2] + zeta[2]) / tau[2],
                     (beta[3, 0] * pastEta(t - theta[3])[0] +
                      beta[3, 1] * pastEta(t - theta[4])[1] +
                      beta[3, 2] * pastEta(t - theta[5])[2] - eta[3] + zeta[3]) / tau[3],
                     (beta[4, 3] * pastEta(t - theta[6])[3] +
                      beta[4, 2] * pastEta(t - theta[7])[2] - eta[4] + zeta[4]) / tau[4]])

# Initial condition and time vector
initCond = np.zeros(5)  # Initial condition for eta
time = np.linspace(0, 10, 100)  # Time vector

# Solve ODE
ETA = odeint(etaFunc, initCond, time)

# Access individual components
eta_0 = ETA[:, 0]
