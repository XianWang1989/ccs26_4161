
import numpy as np
from scipy.integrate import odeint

# Define the time delay
tau = 3.0
delay_steps = 10  # Number of past steps to store
history = np.zeros((delay_steps, 1))  # History array

def etaFunc(Y, t):
    a = 1
    b = 5

    # Update history
    time_index = int(t // (0.1)) % delay_steps  # Update this based on your time step
    history[time_index] = Y[0]  # Store current value in history

    # Get past value (Y(t-tau))
    past_index = int((t - tau) // (0.1)) % delay_steps
    past_value = history[past_index]  # Get value from the history buffer

    dYdt = a * Y[0] + b * past_value

    return [dYdt]

# Initial conditions
initCond = [1.0]
# Time points
time = np.arange(0, 20, 0.1)

# Solve ODE
ETA = odeint(etaFunc, initCond, time)

# Extract results
eta_0 = ETA[:, 0]

import matplotlib.pyplot as plt

# Plot the results
plt.plot(time, eta_0, label='ETA')
plt.xlabel('Time')
plt.ylabel('Value of ETA')
plt.title('Solution of the Differential Equation with Delay')
plt.legend()
plt.show()
