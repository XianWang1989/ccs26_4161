
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Time parameters
tau = 3  # phase shift
time = np.linspace(0, 20, 200)  # time range

# Constants
a = 1
b = 5

# Initialize an array to store past values of Y
past_Y = []

def eqtnSystem(Y, t):
    # Make use of past_Y list to get Y(t-tau)
    if len(past_Y) > 0 and t - tau >= 0:
        # Interpolating past values
        past_value = np.interp(t - tau, time, past_Y)
    else:
        # If there is no valid past value, use 0 or some initial condition
        past_value = 0

    dYdt = a * Y + b * past_value
    return dYdt

# Initial condition
init_cond = 0

# Define a wrapper function to append results to past_Y
def wrapper(Y, t):
    # Update past_Y with the current value of Y
    past_Y.append(Y)
    return eqtnSystem(Y, t)

# Solve the system
ETA = odeint(wrapper, init_cond, time)

# Plot results
plt.plot(time, ETA)
plt.title('Differential Equation with Phase Shift')
plt.xlabel('Time')
plt.ylabel('Y(t)')
plt.grid(True)
plt.show()
