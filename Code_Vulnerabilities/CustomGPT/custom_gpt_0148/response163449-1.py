
import numpy as np
from scipy.integrate import odeint

# Constants
a = 1
b = 5
tau = 3

# To hold past values
history_length = 100  # Adjust based on needs
past_eta = np.zeros((history_length,))

def eqtnSystem(Y, t):
    # Assume Y is a 1D array with eta values
    Y_current = Y[0]

    # Phase shift handling
    if t - tau >= 0:  # Make sure we have past values to reference
        Y_past_index = int(t - tau)
        if Y_past_index >= history_length:
            Y_past_index = history_length - 1  # Clamp index to history size
        Y_past = past_eta[Y_past_index]
    else:
        Y_past = 0  # Default for t < tau

    return a * Y_current + b * Y_past

def etaFunc(A, t, history):
    # Update past values
    index = int(t % history_length)
    history[index] = A[0]  # Assuming A is a 1D array and we want the first component

    return np.array([eqtnSystem(A, t)])

# Time points where we want to compute the solution
time = np.linspace(0, 20, 100)
initCond = np.array([0])  # Initial condition

# Creating a history array to store past eta values
history = np.zeros((history_length,))

# Integrate the system
ETA = odeint(lambda A, t: etaFunc(A, t, history), initCond, time)

# Access the computed values
eta_0 = ETA[:, 0]

# Example output
print(eta_0)
