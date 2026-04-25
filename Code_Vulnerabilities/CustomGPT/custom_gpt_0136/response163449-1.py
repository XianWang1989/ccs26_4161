
import numpy as np
from scipy.integrate import odeint

# Constants
a = 1
b = 5
tau = 3
time_points = np.linspace(0, 20, 100)

# Past values storage
past_values = []

def pastEta(t, stored_values, current_time):
    """Return the past value of eta at time t."""
    if not stored_values or t < 0:
        return 0  # or some default value for out of bounds
    # Find the most recent stored value corresponding to the past time t
    for time, value in reversed(stored_values):
        if time <= t:
            return value
    return 0  # or some default value

def etaFunc(Y, t):
    # Simulate storing the current values
    past_values.append((t, Y.copy()))

    # Use past values for calculation
    eta0 = Y[0]  
    past_eta1 = pastEta(t-tau, past_values, t)

    # Define your differential equations
    dYdt = np.array([
        a * eta0 + b * past_eta1,
        # Add further equations for additional eta components...
    ])

    return dYdt

# Initial conditions
initCond = [0]  # Initialize with desired initial values

# Solve the system of ODEs
ETA = odeint(etaFunc, initCond, time_points)

# Access results
eta0 = ETA[:, 0]
print(eta0)
