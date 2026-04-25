
import numpy as np
from scipy.integrate import odeint

# Define the constants
a = 1
b = 5
tau = 3

# Initialize storage for past values
past_values = []

def etaFunc(Y, t):
    global past_values
    Y_current = Y[0]

    # Store the current value for later access
    if len(past_values) < int(tau):
        past_values.append(Y_current)
    else:
        past_values.pop(0)  # Maintain fixed size for past values
        past_values.append(Y_current)

    # Calculate dY/dt with phase shift
    if t >= tau:
        Y_tau = past_values[-tau]  # Get the value tau time units in the past
    else:
        Y_tau = 0  # Default value for Y(t-tau) before the time shift is possible

    dYdt = a * Y_current + b * Y_tau
    return [dYdt]

# Initial conditions
initCond = [0]  # Starting value for Y
time = np.linspace(0, 20, 100)  # Time points

# Compute the solution
ETA = odeint(etaFunc, initCond, time)

# Extract the results
eta_0 = ETA[:, 0]

# You can visualize the result if needed
import matplotlib.pyplot as plt

plt.plot(time, eta_0, label='eta_0')
plt.xlabel('Time')
plt.ylabel('eta_0')
plt.title('Solution of the Differential Equation with Phase Shift')
plt.legend()
plt.show()
