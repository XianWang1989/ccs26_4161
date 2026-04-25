
import numpy as np
from scipy.integrate import odeint

# Define constants
a = 1
b = 5
tau = 3  # time delay
theta = [2, 3, 4]  # example offsets

# Storage for past values
past_eta = []

def eta_func(Y, t):
    """
    Function to define the differential equations with phase shift.
    Y: current values of eta
    t: current time
    """
    # Unpack the current values
    eta = Y[:len(theta)]

    # Create an array to hold the derivatives
    dYdt = np.zeros_like(eta)

    # Calculate past values based on the shifted time
    for i in range(len(theta)):
        # Check if t - theta[i] is in the past
        if t - theta[i] >= 0:
            if len(past_eta) > 0:
                # Find the index of the latest past value
                past_index = max(0, len(past_eta) - 1 - int((t - theta[i]) / dt))
                dYdt[i] = (a * eta[i] + b * past_eta[past_index]) / tau
            else:
                dYdt[i] = (a * eta[i]) / tau  # no past value available
        else:
            dYdt[i] = (a * eta[i]) / tau  # no past value available

    return dYdt

# Initialize conditions and parameters
init_cond = [0, 0, 0]  # initial values of eta
end_time = 20
dt = 0.1  # time step
time = np.arange(0, end_time, dt)

# Integrate the ODE
ETA = odeint(eta_func, init_cond, time)

# Update past_eta for future calculations
for t_idx in range(len(time)):
    past_eta.append(ETA[t_idx])  # Store the current eta value

# Example of how to retrieve results
eta_0 = ETA[:, 0]  # First component of ETA
print(eta_0)
