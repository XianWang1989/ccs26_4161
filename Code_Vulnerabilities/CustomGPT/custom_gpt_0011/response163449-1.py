
import numpy as np
from scipy.integrate import odeint
from scipy.interpolate import interp1d

# Time parameters
start_time = 0
end_time = 20
time_steps = 100
time = np.linspace(start_time, end_time, time_steps)

# Constants
a = 1
b = 5
tau = 3

# Store past values of Y for interpolation
past_values = []

def eqtnSystem(Y, t):
    # Assuming past_values is updated in the main function body
    past = interp1d(time[:len(past_values)], past_values, fill_value="extrapolate")(t - tau)
    dYdt = a * Y + b * past
    # Store the current value of Y
    past_values.append(Y)
    return dYdt

# Initial condition
initCond = [5]  # Example initial condition

# Integrate the system of equations
ETA = odeint(eqtnSystem, initCond, time)

# Access each individual component of ETA
eta_0 = ETA[:, 0]

# Example: Print out the result
print("Final values of eta_0 at final time:", eta_0[-1])
