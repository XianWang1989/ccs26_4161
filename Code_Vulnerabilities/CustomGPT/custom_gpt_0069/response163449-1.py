
import numpy as np
from scipy.integrate import odeint

# Define constants
a = 1
b = 5
tau = 3

# Initialize parameters and history
history = []

# Function to compute past values based on the current time and history
def get_past_value(t, delay):
    # Find the index of the history that is relevant for time t - delay
    index = int(t - delay)
    if index < 0 or index >= len(history):
        return 0  # Return 0 if out of bounds (no past value)
    return history[index]

# Define the system of equations
def eqtnSystem(Y, t):
    global history
    Y_current = Y[0]

    # Store the current value in the history for future calls
    history.append(Y_current)

    # Calculate dY/dt using the current and past values
    dYdt = a * Y_current + b * get_past_value(t, tau)

    return [dYdt]

# Initial conditions and time array
initCond = [1]
time = np.linspace(0, 10, 100)

# Integrate the system
ETA = odeint(eqtnSystem, initCond, time)

# Extract results
eta_0 = ETA[:, 0]

# Display results
print(eta_0)
