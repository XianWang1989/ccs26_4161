
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Define constants
a = 1
b = 5
tau = 3

# Initialize a storage for past values
max_delay = 10  # maximum delay for storing past values
past_values = []

def eqtnSystem(Y, t, past):
    # Append current value for future reference
    if len(past) < max_delay:
        past.append(Y)
    else:
        past.pop(0)  # Remove the oldest value to maintain the size
        past.append(Y)  # Add the current value

    # Get past value with the proper phase shift
    Y_tau = past[-tau] if len(past) >= tau else 0  # Ensure we have enough past values

    dYdt = a * Y + b * Y_tau
    return dYdt

# Time settings
time = np.linspace(0, 20, 100)
initCond = [1]  # Initial condition

# Integrate using odeint
past_values = []
ETA = odeint(eqtnSystem, initCond, time, args=(past_values,))

# Plot the results
plt.plot(time, ETA)
plt.xlabel('Time')
plt.ylabel('Y(t)')
plt.title('Solution of the differential equation with delay')
plt.grid()
plt.show()
