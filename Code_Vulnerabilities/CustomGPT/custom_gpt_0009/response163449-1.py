
import numpy as np
from scipy.integrate import odeint

# Define parameters
a = 1
b = 5
tau = 3  # Time delay

# Initialize history buffer
history_size = 100  # Number of past values to keep
history = np.zeros(history_size)

# Function to return past value, ensuring it is cyclic
def past_value(t):
    index = int(t) % history_size  # Index for cyclic access
    return history[index]

# Function that defines the differential equation system
def eqtnSystem(Y, t):
    # Store the current value for this time point
    idx = int(t) % history_size
    history[idx] = Y[0]  # Assuming Y is a 1D array

    return [a * Y[0] + b * past_value(t - tau)]

# Initial conditions and time points
initCond = [0]
time = np.linspace(0, 100, 1000)

# Solve the ODE
ETA = odeint(eqtnSystem, initCond, time)

# Now you can access ETA array like ETA[:, 0]
