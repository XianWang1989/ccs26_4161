
import numpy as np
from scipy.integrate import odeint

# Parameters
a = 1
b = 5
tau = 3

# Time parameters
time = np.linspace(0, 20, 100)  # From t=0 to t=20 with 100 points
dt = time[1] - time[0]

# Initialize history for Y
history_length = int(tau / dt)  # Number of time steps for tau
Y_history = np.zeros(history_length)

def eqtnSystem(Y, t):
    # Get current and past value of Y
    current_Y = Y
    past_Y = Y_history[int(t - dt) % history_length]  # Use previous value based on history

    # Update the history
    Y_history[int(t % (history_length * dt) / dt)] = current_Y

    return a * current_Y + b * past_Y

# Initial condition
init_cond = [0]  # Starting value for Y

# Solve the ODE
ETA = odeint(eqtnSystem, init_cond, time)

# Access results
eta_0 = ETA[:, 0]

# Example of plotting the result
import matplotlib.pyplot as plt

plt.plot(time, eta_0, label='eta_0')
plt.xlabel('Time')
plt.ylabel('Value of eta_0')
plt.title('Solution of the Differential Equation with Phase Shift')
plt.legend()
plt.show()
