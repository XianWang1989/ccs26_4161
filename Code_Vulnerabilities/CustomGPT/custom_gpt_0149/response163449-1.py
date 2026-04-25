
import numpy as np
from scipy.integrate import odeint

# Define constants
a = 1
b = 5
tau = 3

# Initial conditions and time
initCond = [0.5]  # Example initial condition
time = np.linspace(0, 20, 100)  # Time array

# Placeholder for historical values
history = []

def eqtnSystem(Y, t):
    current_time_index = len(history) - 1  # Get the index of the current time

    # Store the current value of Y
    if current_time_index >= 0:
        history.append(Y[0])

    # Calculate Y(t-tau) if there is enough historical data
    if t > tau and current_time_index >= tau:
        Y_tau = history[current_time_index - tau]
    else:
        Y_tau = Y[0]  # If not enough history, hold the value constant

    # Define the differential equation
    dYdt = a * Y[0] + b * Y_tau
    return [dYdt]

# Run the integration
ETA = odeint(eqtnSystem, initCond, time)

# Accessing the results
eta_0 = ETA[:, 0]

# Visualization or further analysis can be done here
import matplotlib.pyplot as plt

plt.plot(time, eta_0, label='eta_0')
plt.title('Solution of Phase Shifted Equation')
plt.xlabel('Time')
plt.ylabel('eta_0')
plt.legend()
plt.grid()
plt.show()
