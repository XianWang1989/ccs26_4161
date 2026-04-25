
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Define the initial conditions and parameters
tau = 3.0  # delay time
a = 1.0
b = 5.0

# Initialize an empty list to store past values of Y
past_Y = []

def eqtnSystem(Y, t):
    # Ensure that the list tracks up to the current time
    while len(past_Y) <= len(past_Y) + int(tau):
        past_Y.append(Y)  # Store the current Y value

    # Get a past value of Y (for t - tau)
    index_tau = max(0, len(past_Y) - int(tau))  # Ensure index is not out of bounds
    Y_tau = past_Y[index_tau] if index_tau < len(past_Y) else 0

    # Return the derivative
    return a * Y + b * Y_tau

# Time points where we want to solve the system
time = np.linspace(0, 20, 100)

# Initial condition
init_cond = [0.1]  # initial value of Y

# Solve the ODE
ETA = odeint(eqtnSystem, init_cond, time)

# Plotting results
plt.plot(time, ETA)
plt.xlabel('Time')
plt.ylabel('Y(t)')
plt.title('Solution of the ODE with a time delay')
plt.grid()
plt.show()
