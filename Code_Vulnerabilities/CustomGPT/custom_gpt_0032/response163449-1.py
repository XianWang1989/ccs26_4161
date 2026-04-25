
import numpy as np
from scipy.integrate import odeint

# Define constants
a = 1
b = 5
tau = 3

# Initial conditions and time points
initCond = [0]  # Adjust based on your system
time = np.linspace(0, 20, 100)

# Variable to hold past values
past_values = []

# Define the system of equations
def etaFunc(Y, t):
    # Store current value if we have enough previous values
    if t >= tau:
        past_value = past_values[int(t - tau)]
    else:
        past_value = 0  # Default value if no past value available

    # Store the current Y value in the past values list
    past_values.append(Y[0])

    return [a * Y[0] + b * past_value]

# Integrate the ODE
ETA = odeint(etaFunc, initCond, time)

# Extract results
eta_0 = ETA[:, 0]

# Plotting (optional)
import matplotlib.pyplot as plt

plt.plot(time, eta_0, label='eta')
plt.xlabel('Time')
plt.ylabel('eta(t)')
plt.title('Solution of Phase-Shifted ODE')
plt.legend()
plt.show()
