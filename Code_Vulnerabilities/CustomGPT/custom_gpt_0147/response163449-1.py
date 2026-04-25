
import numpy as np
from scipy.integrate import odeint

# Constants definition
a = 1
b = 5
tau = 3

# Initialize the history buffer
buffer_size = 100  # Length of the buffer
history = np.zeros((buffer_size, 2))  # Adjust dimensions based on your system

def pastEta(t, history, current_time):
    """Estimate past eta values based on the buffer."""
    # Calculate the appropriate index for t - tau
    index = int(np.floor(current_time - t))
    if 0 <= index < buffer_size:
        return history[index]  # Return the past eta value
    else:
        return np.zeros(2)  # Return test value for out of bounds

def etaFunc(A, t):
    global history
    current_time = int(t)

    # Update history buffer
    history[current_time % buffer_size] = A

    # Using pastEta to evaluate the past values
    past_eta_values = pastEta(t - tau, history, current_time)

    # Define the equations using current and past values
    return np.array([a * A[0] + b * past_eta_values[0],  # For eta[0]
                     a * A[1] + b * past_eta_values[1]])  # For eta[1]

# Time array
time = np.linspace(0, 100, 1000)
init_cond = np.array([0.0, 0.0])  # Initial conditions for eta[0] and eta[1]

# Solve the ODE
ETA = odeint(etaFunc, init_cond, time)

# Extract individual components
eta_0 = ETA[:, 0]
eta_1 = ETA[:, 1]

