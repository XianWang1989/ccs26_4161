
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Parameters
a = 1
b = 5
tau = 3  # Time delay
time = np.linspace(0, 20, 100)  # Time points
initCond = [0]  # Initial condition

# Function to retrieve past values
def past_eta(t, history, time_points):
    if t < 0:
        return 0  # Return 0 for times before we start
    # Find the closest time in the history for t
    idx = np.searchsorted(time_points, t)
    if idx == 0:
        return 0  # If we're before the history, return 0
    return history[idx - 1]

# Differential equation system
def eqtnSystem(A, t, history, time_points):
    y = A[0]

    # Retrieve past value
    y_tau = past_eta(t - tau, history, time_points)

    # Return the derivatives
    return [a * y + b * y_tau]

# Initialize history storage
history = []
time_points = np.zeros(len(time))

# Function to store previous values over time
def store_history(eta, t):
    history.append(eta[0])
    time_points[len(history) - 1] = t

# Integration
ETA = []
for i, t in enumerate(time):
    # Solve the ODE
    sol = odeint(eqtnSystem, initCond, [t], args=(history, time_points))
    ETA.append(sol[0])
    store_history(sol, t)

ETA = np.array(ETA)

# Plotting the results
plt.plot(time, ETA[:, 0], label='y(t)')
plt.xlabel('Time')
plt.ylabel('Function value')
plt.title('Differential Equation with Phase Shift')
plt.legend()
plt.grid()
plt.show()
