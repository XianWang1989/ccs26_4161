
import numpy as np
from scipy.integrate import odeint

# Parameters
a = 1.0
b = 5.0
tau = 3.0

# Time array
time = np.linspace(0, 20, 200)

# Initial condition
initCond = [1.0]  # Initial value for Y

# Function to store past values and include time delay
def eqtnSystem(Y, t, history):
    # Ensure history is updated
    if t > tau:
        # Retrieve the past value
        Y_past = history[int((t - tau) / (time[1] - time[0]))]
    else:
        Y_past = 0  # Assume zero if we don't have historical data yet

    # Update history with the current Y value
    history.append(Y[0])

    # Return the derivative
    dYdt = a * Y[0] + b * Y_past
    return [dYdt]

# History to store past values
history = [initCond[0]]

# Solve the ODE
ETA = odeint(eqtnSystem, initCond, time, args=(history,))

# Extract individual components
Y = ETA[:, 0]

# Plotting (optional)
import matplotlib.pyplot as plt

plt.plot(time, Y)
plt.xlabel('Time')
plt.ylabel('Y(t)')
plt.title('Solution of Y(t) with delayed feedback')
plt.grid()
plt.show()
