
import numpy as np
from scipy.integrate import odeint

# Parameters
a = 1
b = 5
tau = 3.0  # time delay
time_steps = 100
time = np.linspace(0, 30, time_steps)  # time vector
init_cond = [0]  # initial condition for Y

# History buffer to store past values of Y
history_length = int(tau / (time[1] - time[0]))  # number of past steps to remember
Y_history = [0] * history_length  # initialize history

def eqtnSystem(Y, t):
    # Update the history
    Y_history.append(Y[0])  # store current value
    if len(Y_history) > history_length:
        Y_history.pop(0)  # maintain fixed size

    # Access the delayed value Y(t-tau)
    delayed_Y = Y_history[0]  # value at time (t-tau)

    # Differential equation
    dYdt = a * Y[0] + b * delayed_Y
    return [dYdt]

# Solve the ODE
ETA = odeint(eqtnSystem, init_cond, time)

# Extract results
eta_0 = ETA[:, 0]

# Let's visualize the result (optional)
import matplotlib.pyplot as plt

plt.plot(time, eta_0, label='Y(t)')
plt.xlabel('Time')
plt.ylabel('Y')
plt.legend()
plt.title('ODE Solution with Phase Shift')
plt.grid()
plt.show()
