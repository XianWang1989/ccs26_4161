
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Define parameters
a = 1.0
b = 5.0
tau = 3.0

# Time span
time = np.linspace(0, 20, 100)

# Initial condition
initCond = [0.0]

# Create an array to store the values of Y over time
history = np.zeros((len(time), len(initCond)))

def eqtnSystem(Y, t, history):
    Y = Y[0]  # Since we're using a single variable, unpack it
    # Calculate the index for the past value based on the time shift
    past_index = np.searchsorted(time, t - tau)  # Find the index of t-tau
    past_value = history[past_index-1, 0] if past_index > 0 else 0  # Use the previous value in history

    dYdt = a * Y + b * past_value  # Apply the equation with the delayed component
    return [dYdt]

# Time-loop to compute the values dynamically
for i, t in enumerate(time):
    # Update history before computing the new value
    if i > 0:
        initCond[0] = eqtnSystem(initCond, t, history)[0]  # Compute new value
    history[i] = initCond  # Store the current state in history

# Solve using odeint
ETA = odeint(eqtnSystem, initCond, time, args=(history,))

# Plot the results
plt.plot(time, ETA[:, 0], label='Y(t)')
plt.title("Differential Equation with Phase Shift")
plt.xlabel("Time")
plt.ylabel("Y")
plt.legend()
plt.grid()
plt.show()
