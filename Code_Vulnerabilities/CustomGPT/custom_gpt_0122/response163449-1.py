
import numpy as np
from scipy.integrate import odeint

# Constants
a = 1
b = 5
tau = 3
theta = [3, 1, 2, 1, 4, 4]  # Example values, adjust as needed

# Past values storage
def past_values(t, t_values, Y_values):
    # Return interpolated past values if they exist
    if t < t_values[0]:  # No past value exists
        return np.zeros(Y_values.shape)
    else:
        idx = np.searchsorted(t_values, t) - 1
        return Y_values[idx]

# Define the system of equations
def etaFunc(Y, t, t_values, Y_values):
    # Interpolate past values
    pastY = past_values(t - tau, t_values, Y_values)
    return np.array([
        a * Y[0] + b * pastY[0],  # Example equation for eta_0
        (a * Y[1] + b * pastY[1]) / tau,  # eta_1
        (a * Y[2] + b * pastY[2]) / tau,  # eta_2
        (b * pastY[3] - Y[3]) / tau,  # eta_3
        (b * pastY[4] - Y[4]) / tau   # eta_4
    ])

# Initial conditions
initCond = np.zeros(5)
time = np.linspace(0, 20, 100)

# To store past values
Y_values = []
t_values = []

# Run the integration
def solve_odes(initCond, time):
    for t in time:
        sol = odeint(etaFunc, initCond, [t], args=(t_values, Y_values))
        Y_values.append(sol[-1])
        t_values.append(t)
        initCond = sol[-1]

solve_odes(initCond, time)

# Convert to array for easier access later
Y_values = np.array(Y_values)

# Now you can access different components
print(Y_values[:, 0])  # eta_0 over time
