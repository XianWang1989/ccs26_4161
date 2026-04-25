
import numpy as np
from scipy.integrate import odeint

# Constants
a = 1
b = 5
tau = 3

# History of Y values
history = []

def eqtnSystem(Y, t):
    # Keep track of the historical values
    history.append(Y)

    # Get the past value Y(t-tau) using interpolation
    if t - tau < 0:
        Y_past = 0  # Default value before history starts
    else:
        idx = int(t - tau)  # Find the index for tau back in history
        if idx >= len(history):  
            Y_past = history[idx]  # Get value from history
        else:
            # Interpolation would be useful here if necessary
            Y_past = history[-1]  # Adjust this logic as needed

    # Return the derivative
    return a * Y + b * Y_past

# Define the time points where we want the solution
time = np.linspace(0, 20, 100)
initCond = [1]  # Initial condition for Y(0)

# Solve the ODE
ETA = odeint(eqtnSystem, initCond, time)

# Extracting the results
Y_values = ETA[:, 0]

# Plot the result to visualize (optional)
import matplotlib.pyplot as plt
plt.plot(time, Y_values, label='Y(t)')
plt.xlabel('Time')
plt.ylabel('Y')
plt.title('Solution of ODE with Phase Shift')
plt.legend()
plt.show()
