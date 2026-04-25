
import numpy as np
from scipy.integrate import odeint

# Constants
a = 1
b = 5
tau = 3
theta = [1, 2, 3, 4, 5, 6]  # example values

# Initialize state history
history_length = 100  # Length of history to keep track of
eta_history = np.zeros((history_length, 5))  # Change 5 to the number of variables + 1 for current value

# Define the function to retrieve past values
def pastEta(t_minus_tau, current_time):
    if t_minus_tau < 0 or t_minus_tau > current_time:
        return np.zeros(5)  # Return zero if out of bounds
    else:
        index = int(t_minus_tau) % history_length
        return eta_history[index]

def etaFunc(A, t):
    global eta_history
    # Update history
    eta_history[int(t) % history_length] = A

    # Compute the rates of change
    return np.array([
        (a * A[0] + b * pastEta(t - theta[0], t)[0]) / tau,
        (a * A[1] + b * pastEta(t - theta[1], t)[1]) / tau,
        (a * A[2] + b * pastEta(t - theta[2], t)[2]) / tau,
        (b * pastEta(t - theta[3], t)[3] - A[3] + 1) / tau,  # Replace +1 with zeta[3] if needed
        (b * pastEta(t - theta[4], t)[4] - A[4] + 1) / tau   # Replace +1 with zeta[4] if needed
    ])

# Initial conditions and time points
initCond = np.array([1, 1, 1, 1, 1])  # Initial values for eta
time = np.linspace(0, 100, 100)  # Time points

# Solve the system
ETA = odeint(etaFunc, initCond, time)

# Example of accessing components
eta_0 = ETA[:, 0]
print(eta_0)
