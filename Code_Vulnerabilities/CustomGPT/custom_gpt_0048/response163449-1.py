
import numpy as np
from scipy.integrate import odeint

# Define parameters
a = 1.0
b = 5.0
tau = 3.0 
time_points = np.linspace(0, 20, 100)  # Adjust time range as needed

# Initialize a buffer for past values, max length of tau
delay_points = int(tau / (time_points[1] - time_points[0])) + 1
past_values = np.zeros(delay_points)

# Function to calculate the system of equations
def eqtnSystem(Y, t):
    # Shift the past values
    past_values[1:] = past_values[:-1]  # Shift past values
    past_values[0] = Y                   # Update current value

    Y_tau = past_values[-1]               # Get the value at t - tau

    dYdt = a * Y + b * Y_tau
    return dYdt

# Initial condition
initCond = [0]  # Example initial condition; adjust as needed

# Solve the ODE
ETA = odeint(eqtnSystem, initCond, time_points)

# Extract the results
eta_0 = ETA[:, 0]

# Plot or process eta_0 as needed
import matplotlib.pyplot as plt

plt.plot(time_points, eta_0)
plt.title("Solution for eta_0 over time")
plt.xlabel("Time")
plt.ylabel("eta_0")
plt.grid()
plt.show()
