
import numpy as np
from scipy.integrate import odeint
from scipy.interpolate import interp1d

# Constants and parameters
a = 1
b = 5
tau = 3

# Define your initial conditions and time points
initCond = [0]  # Example initial condition
time = np.linspace(0, 10, 100)  # Time points

# To store the calculated values of eta
eta_history = []

def pastEta(t, time_points, eta_values):
    """ Interpolate to find past values of eta. """
    interp_func = interp1d(time_points, eta_values, fill_value="extrapolate", bounds_error=False)
    return interp_func(t)

def etaFunc(A, t, time_points, eta_values):
    global eta_history
    Y = A[0]

    # Store the current value
    eta_history.append(Y)

    # Get past values with interpolation
    fetched_past = pastEta(t - tau, time_points, eta_history)

    # Define the equation
    dydt = a * Y + b * fetched_past  # Using the fetched past value

    return [dydt]

# Run the integration
ETA = odeint(etaFunc, initCond, time, args=(time, eta_history))

# Access components of ETA
eta_0 = ETA[:, 0]
