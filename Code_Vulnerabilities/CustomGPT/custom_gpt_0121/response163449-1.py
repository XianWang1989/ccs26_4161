
import numpy as np
from scipy.integrate import odeint

# Constants
a = 1
b = 5
tau = 3

# Time parameters
time = np.linspace(0, 50, 1000)  # Time from 0 to 50 with 1000 steps
initCond = [1, 0, 0, 0, 0]  # Initial conditions for eta

# Store past values of eta in a circular buffer
past_eta = []

def etaFunc(A, t):
    global past_eta
    # Append current value of eta
    if len(past_eta) < int(tau) + 1:
        past_eta.append(A.copy())
    else:
        past_eta.pop(0)
        past_eta.append(A.copy())

    # Calculate phase-shifted values
    past_eta_values = [past_eta[i] if i < len(past_eta) else 0 for i in range(len(past_eta))]

    # Define your equations; here we'll assume 5 components
    dEta = np.zeros_like(A)
    dEta[0] = a * A[0] + b * past_eta_values[0][0]  # Y(t)
    dEta[1] = a * A[1] + b * past_eta_values[1][1]  # Y(t-tau)
    dEta[2] = a * A[2] + b * past_eta_values[2][2]
    dEta[3] = (b * (past_eta_values[3][0] + past_eta_values[4][1])) / tau
    dEta[4] = (b * (past_eta_values[5][2])) / tau

    return dEta

# Integrate the equations over time
ETA = odeint(etaFunc, initCond, time)

# Access individual components
eta_0 = ETA[:, 0]
eta_1 = ETA[:, 1]
eta_2 = ETA[:, 2]
eta_3 = ETA[:, 3]
eta_4 = ETA[:, 4]

# Plots or further analysis can be done here
