
import numpy as np
from scipy.integrate import odeint

# Define your constants
a = 1
b = 5
tau = 3

# Define a function to compute past values
def past_eta(t, t_values, eta_values):
    # Find the last index with t(tau) < t
    idx = np.where(t_values <= (t - tau))[0]
    return eta_values[idx[-1]] if idx.size > 0 else 0

# Define the system of equations
def etaFunc(A, t, t_values, eta_values):
    current_eta = A
    # Store current eta
    eta_values.append(current_eta) 
    t_values.append(t)

    # Calculate the contributions
    past_value = past_eta(t, t_values, eta_values)

    # Return the rates of change
    return np.array([a * current_eta[0] + b * past_value])

# Initialize variables
initCond = [0]  # initial condition for eta
time = np.linspace(0, 20, 100)  # time points to integrate over

# Store past eta and time values
t_values = []
eta_values = []

# Solve the ODE with the initial conditions
ETA = odeint(etaFunc, initCond, time, args=(t_values, eta_values))

# Extract each component of ETA
eta_0 = ETA[:, 0]
