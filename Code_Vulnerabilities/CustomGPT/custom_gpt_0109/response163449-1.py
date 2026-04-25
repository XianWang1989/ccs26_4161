
import numpy as np
from scipy.integrate import odeint

# Define parameters
a = 1
b = 5
tau = 3

# Initial conditions
initCond = [0, 0, 0, 0, 0]  # Example initial conditions for eta

# Time points
time = np.linspace(0, 10, 100)

# Store past values in a list
past_eta = []

# Define the system of equations
def etaFunc(Y, t):
    # Append the current value to the past_eta list
    past_eta.append(Y.copy())

    # Only use past values if they exist and are within the time range
    if t > tau:
        past_values = np.array(past_eta)[-int(tau):]  # Get most recent tau seconds of values
        past_Y = past_values[:, 0]  # Assuming Y corresponds to the first component
    else:
        past_Y = np.zeros(len(Y))  # No past values available yet

    # Calculate the derivatives
    dYdt = np.zeros_like(Y)
    dYdt[0] = a * Y[0] + b * past_Y[0]  # Example for dY/dt for component 0
    # ... Add more equations as needed
    return dYdt

# Integrate using odeint
ETA = odeint(etaFunc, initCond, time)

# Access the results
eta_0 = ETA[:, 0]
eta_1 = ETA[:, 1]
# ... and so on
