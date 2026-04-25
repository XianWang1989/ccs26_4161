
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Define constants
a = 1
b = 5
tau = 3

# Time settings
time = np.linspace(0, 20, 100)  # Example time from 0 to 20 seconds
initCond = [1, 0, 0, 0, 0]  # initial conditions for eta

# Store past eta values
past_eta_values = []

# Define the system of equations
def etaFunc(A, t):
    global past_eta_values
    # Check if we have past values to use
    if len(past_eta_values) == 0:
        past_eta_values = [A]  # initialize with current values

    # Update past values
    if t > tau:  # only store after the delay period
        past_eta_values.append(A)

    # Calculate the current values, applying the phase shift
    current_eta = np.zeros_like(A)
    current_eta[0] = a * A[0] + b * get_past_value(t - tau, 0)  # Y(t) + Y(t-tau)
    current_eta[1] = A[1]  # modify based on your system
    current_eta[2] = A[2]  # modify based on your system
    current_eta[3] = A[3]  # modify based on your system
    current_eta[4] = A[4]  # modify based on your system

    return current_eta

def get_past_value(time, index):
    """Retrieve past value based on time and index."""
    if time < 0 or len(past_eta_values) == 0:
        return 0  # Return zero if no past value exists
    past_index = int(time // (time[1] - time[0]))  # Get index based on time step size
    if past_index < len(past_eta_values):
        return past_eta_values[past_index][index]
    else:
        return 0  # Return zero if past index is out of bounds

# Integrate the system
ETA = odeint(etaFunc, initCond, time)

# Plot results
plt.plot(time, ETA[:, 0], label='eta_0')
plt.plot(time, ETA[:, 1], label='eta_1')
plt.plot(time, ETA[:, 2], label='eta_2')
plt.legend()
plt.xlabel('Time')
plt.ylabel('Values of eta')
plt.title('Solutions of the differential equations')
plt.show()
