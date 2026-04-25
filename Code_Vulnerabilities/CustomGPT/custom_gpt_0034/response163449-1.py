
import numpy as np
from scipy.integrate import odeint
from scipy.interpolate import interp1d

# Constants
a = 1
b = 5
tau = 3

# Define the system of equations
def eqtnSystem(Y, t, Y_history, time_history):
    # Interpolate past values
    if t - tau < 0:
        Y_tau = 0  # Handle initial condition if t - tau is less than 0
    else:
        interp_func = interp1d(time_history, Y_history, bounds_error=False, fill_value="extrapolate")
        Y_tau = interp_func(t - tau)

    dYdt = a * Y + b * Y_tau
    return dYdt

# Time variables
time = np.linspace(0, 10, 100)  # Total simulation time
init_cond = [0]  # Initial condition for Y

# Arrays to hold the history of Y
Y_history = []
time_history = []

# ODE solving loop to capture history
for t in time:
    if len(Y_history) == 0:  # First step
        Y_current = init_cond[0]
    else:
        Y_current = odeint(eqtnSystem, Y_history[-1], [t], args=(Y_history, time_history))[0][0]

    # Store results
    Y_history.append(Y_current)
    time_history.append(t)

# Convert to array for easier indexing
Y_history = np.array(Y_history)
time_history = np.array(time_history)

# Plotting results
import matplotlib.pyplot as plt

plt.figure()
plt.plot(time_history, Y_history, label='Y(t)')
plt.title('Differential Equation with Phase Shift')
plt.xlabel('Time')
plt.ylabel('Y(t)')
plt.legend()
plt.show()
