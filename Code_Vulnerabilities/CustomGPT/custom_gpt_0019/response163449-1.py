
import numpy as np
from scipy.integrate import odeint
from collections import deque

# Parameters
a = 1
b = 5
tau = 3
num_points = 100  # Number of time points
dt = 0.1  # Time step
time = np.arange(0, num_points * dt, dt)

# Initialize past values storage
past_Y = deque(maxlen=int(tau / dt))
initCond = [1]  # Initial condition for Y

def eqtnSystem(Y, t):
    # Update past values
    if len(past_Y) < past_Y.maxlen:
        past_Y.append(Y[0])
    else:
        past_Y.append(Y[0])

    if t < tau:
        past_value = 0  # Use initial value if not enough time has passed
    else:
        past_value = past_Y[-int(tau / dt) - 1]  # Get the value from tau seconds ago

    dYdt = a * Y[0] + b * past_value
    return [dYdt]

# Integrate the system
ETA = odeint(eqtnSystem, initCond, time)

# Access the results
eta_0 = ETA[:, 0]

# For visualization (optional)
import matplotlib.pyplot as plt

plt.plot(time, eta_0)
plt.title('Dynamics of Y with Phase Shift')
plt.xlabel('Time')
plt.ylabel('Y(t)')
plt.show()
