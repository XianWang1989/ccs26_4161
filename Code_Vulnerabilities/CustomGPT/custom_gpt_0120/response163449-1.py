
import numpy as np
from scipy.integrate import odeint

# Time parameters
tau = 3  # Phase shift
time = np.linspace(0, 20, 100)  # Time vector

# Initialize a history to store past values of eta
eta_history = np.zeros((len(time), 2))  # Adjust size as needed (2 for eta_0 and eta_1)

# Differential equation system
def etaFunc(eta, t):
    y0 = eta[0]  # Current value of eta_0
    y1 = eta[1]  # Current value of eta_1

    # Get past values based on time
    if t - tau >= 0:
        past_index = np.searchsorted(time, t - tau)
        past_eta_0 = eta_history[past_index, 0]  # past eta_0
        past_eta_1 = eta_history[past_index, 1]  # past eta_1
    else:
        past_eta_0 = 0
        past_eta_1 = 0

    # Constants
    a = 1
    b = 5

    # Define the equations
    dYdt = [a * y0 + b * past_eta_0, a * y1 + b * past_eta_1]

    return dYdt

# Initial conditions
initCond = [1, 0]  # Example initial conditions for (eta_0, eta_1)

# Solve the ODE
ETA = odeint(etaFunc, initCond, time)

# Store the results for future reference
for i in range(len(time)):
    eta_history[i, :] = ETA[i, :]

# Access results
eta_0 = ETA[:, 0]
eta_1 = ETA[:, 1]

# Output the results
print("eta_0:", eta_0)
print("eta_1:", eta_1)
