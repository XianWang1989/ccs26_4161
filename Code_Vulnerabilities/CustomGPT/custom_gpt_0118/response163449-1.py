
import numpy as np
from scipy.integrate import odeint

# Define constants
a = 1
b = 5
tau = 3
time_steps = 100
time = np.linspace(0, 10, time_steps)

# To store past values of eta
past_eta = []

def etaFunc(A, t):
    # Ensure there's enough past data
    if len(past_eta) < tau:
        past_vals = [0] * (tau - len(past_eta)) + past_eta
    else:
        past_vals = past_eta[-tau:]

    # Define your differential equation
    dYdt = a * A + b * past_vals[-1]  # Equivalent to Y(t-tau)

    # Append the current value to past_eta
    past_eta.append(A)

    return dYdt

# Initial condition
initCond = [0]  # Replace with your specific initial condition

# Solve the ODE
ETA = odeint(etaFunc, initCond, time)

# Access specific components
eta_0 = ETA[:, 0]

# Output the result
print(eta_0)
