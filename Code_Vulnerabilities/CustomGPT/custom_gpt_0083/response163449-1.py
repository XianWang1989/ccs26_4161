
import numpy as np
from scipy.integrate import odeint
from scipy.interpolate import interp1d

# Constants
a = 1
b = 5
tau = 3
theta = [1, 2, 3, 4, 5]  # Example shift values
time = np.linspace(0, 20, 100)  # Time span
initCond = [0, 0, 0, 0, 0]  # Initial conditions

# To store eta values
etas = []

def etaFunc(A, t, past_eta_func):
    # Ensure past values are accessible via interpolation
    past_Y = past_eta_func(t - np.array(theta))  # Get past eta values
    return np.array([
        a * A[0] + b * past_Y[0] / tau, 
        a * A[1] + b * past_Y[1] / tau, 
        a * A[2] + b * past_Y[2] / tau,
        a * A[3] + b * past_Y[3] / tau,
        a * A[4] + b * past_Y[4] / tau
    ])

# Integrate the ODE
for t_val in time:
    # Collect current eta values for interpolation
    etas.append(initCond)

# Create an interpolation function for the past values
past_eta_func = interp1d(time, etas, axis=0, fill_value="extrapolate")

# Integrate
ETA = odeint(etaFunc, initCond, time, args=(past_eta_func,))

# Extract individual components
eta_0 = ETA[:, 0]
eta_1 = ETA[:, 1]
# Continue for other components...

# You can plot or analyze eta_0, eta_1, etc. as needed
