
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Constants
a = 1
b = 5
tau = 3

# Store past values of eta
eta_history = []

def pastEta(t, time_points, eta_values):
    """Get interpolated value of eta at time t from provided time points and values."""
    if t < 0 or t < time_points[0]:
        return 0  # Return 0 or some default value if t is out of range.

    return np.interp(t, time_points, eta_values)

def etaFunc(A, t):
    global eta_history
    # Add current value to the history
    eta_history.append(A.copy())

    # Make sure to keep only the last few values based on tau
    if len(eta_history) > 100:  # Define how many past values to keep
        eta_history.pop(0)

    time_points = np.linspace(0, t, len(eta_history))  # Time points corresponding to the values

    # Past eta calculations
    past_eta_tau = pastEta(t - tau, time_points, [eta[0] for eta in eta_history])

    # Derivative calculations
    return a * A + b * past_eta_tau

# Initial conditions
initCond = [1]  # You need to define appropriate initial conditions
time = np.linspace(0, 20, 500)  # Time array

# Integrate using odeint
ETA = odeint(etaFunc, initCond, time)

# Plot results
plt.plot(time, ETA)
plt.xlabel('Time')
plt.ylabel('ETA')
plt.title('Solutions for Differential Equations with Phase Shift')
plt.legend(['eta_0'])
plt.show()
