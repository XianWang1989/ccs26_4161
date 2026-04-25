
import numpy as np
from scipy.integrate import odeint

# Define the system of equations with phase shift
def etaFunc(A, t, past_values, tau):
    # Define constants
    a = 1
    b = 5

    # Retrieve past values based on time condition
    Y_tau = past_values[int(t - tau)] if (t - tau) >= 0 else 0  # handle past values with a boundary condition

    # Calculate dY/dt
    dYdt = a * A + b * Y_tau
    return dYdt

# Initialize parameters
initCond = [1, 1, 1, 1, 1]  # Initial conditions for eta_0, eta_1, ..., eta_4
time = np.linspace(0, 10, 100)  # Time points
tau = 3  # Delay

# Array to store past values
past_values = np.zeros((len(time), len(initCond)))

# Store the initial condition in past_values
past_values[0] = initCond

# Solve ODE using odeint
ETA = np.zeros((len(time), len(initCond)))
ETA[0] = initCond

for i in range(1, len(time)):
    # Get the current time
    t = time[i]

    # Call etaFunc to compute the derivative
    dY = etaFunc(ETA[i-1], t, ETA[:i], tau)

    # Update the value using Euler integration (or you can use more sophisticated methods)
    ETA[i] = ETA[i-1] + dY * (t - time[i - 1])

# Example: Get individual components
eta_0 = ETA[:, 0]
eta_1 = ETA[:, 1]
# Add more components as needed

# Plot or analyze your results as required
import matplotlib.pyplot as plt

plt.plot(time, eta_0, label='eta_0')
plt.plot(time, eta_1, label='eta_1')
plt.legend()
plt.xlabel('Time')
plt.ylabel('Values')
plt.title('Phase Shifted Differential Equations')
plt.show()
