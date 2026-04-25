
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Constants
a = 1.0
b = 5.0
tau = 3.0  # phase shift

# Global variable to store past states of eta
history = []

def eqtnSystem(Y, t):
    # Append the current value of Y to the history
    history.append(Y[0])

    # Ensure we have enough historical data to reference Y(t - tau)
    if t - tau < 0 or len(history) < 2:
        # If we don't have enough data, return an equation not dependent on the past
        return [a * Y[0]]

    # Calculate the index for past values
    past_index = int(t - tau)  # Getting the integer index for the time

    # Check to not exceed history bounds
    if past_index >= len(history):
        past_index = len(history) - 1  # Use the most recent value available

    # dY/dt equation
    dYdt = a * Y[0] + b * history[past_index]
    return [dYdt]

# Time points to evaluate the ODE
time = np.linspace(0, 20, 100)
initCond = [1.0]  # Initial condition

# Clear history before solving
history.clear()

# Solve the ODE
ETA = odeint(eqtnSystem, initCond, time)

# Plotting
plt.plot(time, ETA, label='eta(t)')
plt.xlabel('Time')
plt.ylabel('eta')
plt.title('Differential Equation with Phase Shift')
plt.legend()
plt.show()
