
import numpy as np
from scipy.integrate import odeint

# Parameters
a = 1.0
b = 5.0
tau = 3.0  # The time shift

# Time parameters
time = np.linspace(0, 20, 100)  # Time vector

# Initial condition
initCond = [0.0]  # Starting value, this can be a vector for multiple equations

# Buffer size for past values
buffer_size = int(tau / (time[1]-time[0])) + 1  # Adjust based on time step
past_values = np.zeros((buffer_size, len(initCond)))
past_values_idx = 0

def eqtnSystem(Y, t):
    # Store current value in the buffer
    global past_values, past_values_idx
    past_values[past_values_idx] = Y

    # Calculate index for Y(t-tau)
    idx = (past_values_idx - int(tau / (time[1]-time[0]))) % buffer_size
    Y_tau = past_values[idx] if (past_values_idx >= int(tau / (time[1]-time[0]))) else 0  # Zero if not enough history

    # Update past values index
    past_values_idx = (past_values_idx + 1) % buffer_size

    # Return the derivatives
    return [a * Y[0] + b * Y_tau[0]]

# Solve the system of differential equations
ETA = odeint(eqtnSystem, initCond, time)

# Fetch individual components
eta_0 = ETA[:, 0]

# Display results (for example purposes)
import matplotlib.pyplot as plt

plt.plot(time, eta_0)
plt.title('Solution of the Differential Equation with Phase Shift')
plt.xlabel('Time')
plt.ylabel('Y(t)')
plt.grid()
plt.show()
