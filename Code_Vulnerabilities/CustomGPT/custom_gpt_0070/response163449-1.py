
import numpy as np
from scipy.integrate import odeint

# Define global variables to store past values
past_eta = []

def etaFunc(A, t, theta, beta, gamma, zeta, tau):
    global past_eta

    # Ensure past_eta has enough history; if not, pad with zeros or previous values
    if len(past_eta) < len(A) or t < max(theta):
        past_eta.append(A.copy())  # Store the current state for future reference
    elif len(past_eta) > len(A):
        past_eta = past_eta[-len(A):]  # Keep only the most recent values

    # Calculate the phase-shifted terms based on past eta
    current_eta = np.zeros_like(A)

    for i in range(len(A)):
        if t - theta[i] > 0:
            past_index = int((t - theta[i]) // (time[1] - time[0]))
            if past_index < len(past_eta):
                current_eta[i] = past_eta[past_index][i]

    # Differential equations
    return [
        (gamma[i, i] * xi(t - theta[i])[i] - A[i] + zeta[i]) / tau[i] for i in range(len(A))
    ]

# Initial conditions and parameters
initCond = np.zeros(5)  # Example initial condition
time = np.linspace(0, 10, 100)  # Time points
theta = [1, 2, 3, 4, 5]  # Phase shifts
beta = np.random.rand(5, 5)  # Example parameters
gamma = np.random.rand(5, 5)  # Example parameters
zeta = np.random.rand(5)  # Example parameters
tau = [1, 1, 1, 1, 1]  # Time constants

# Perform integration
ETA = odeint(etaFunc, initCond, time, args=(theta, beta, gamma, zeta, tau))

# Access the results
eta_0 = ETA[:, 0]
print("eta_0:", eta_0)
