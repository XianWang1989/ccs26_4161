
import numpy as np
from scipy.integrate import odeint

# Function to simulate past values of Y using interpolation
def pastY(t, times, Y_values, tau):
    if t - tau < times[0]:
        return Y_values[0]  # Return the initial condition if it's out of bounds
    for i in range(1, len(times)):
        if times[i] > t - tau:
            # Interpolate the Y value at the time (t-tau)
            return np.interp(t - tau, [times[i-1], times[i]], [Y_values[i-1], Y_values[i]])
    return Y_values[-1]  # Return the last known value if t-tau is beyond the last time

# System of differential equations
def eqtnSystem(Y, t, history_times, history_Y):
    a = 1
    b = 5
    tau = 3

    Y_past = pastY(t, history_times, history_Y, tau)
    dYdt = a * Y + b * Y_past
    return [dYdt]

# Initial conditions
initCond = [0]
time = np.linspace(0, 20, 100)

# To keep track of history
history_times = []
history_Y = []

# Use a function to simulate the evolution over time
def simulate():
    Y = initCond
    for t in time:
        history_times.append(t)
        Y_new = odeint(eqtnSystem, Y, [t], args=(history_times, history_Y))
        history_Y.append(Y_new[0, 0])  # Store the latest Y value
        Y = Y_new[0]

    return np.array(history_Y)

# Run the simulation
ETA = simulate()

# Example usage: Getting individual components
print(ETA)
