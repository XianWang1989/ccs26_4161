
import numpy as np
from scipy.integrate import odeint
from scipy.interpolate import interp1d

# Define your parameters
a = 1
b = 5
tau = 3

# Function to get past values using interpolation
def pastEta(t_values, eta_values, t):
    # Filter the values to get past times
    valid_indices = t_values < t
    if any(valid_indices):
        t_past = t_values[valid_indices]
        eta_past = eta_values[valid_indices]
        interp_func = interp1d(t_past, eta_past, fill_value="extrapolate", bounds_error=False)
        return interp_func(t)
    else:
        return np.zeros(len(eta_values[0]))  # or an appropriate default value

# Define the system of equations
def etaFunc(eta, t, t_values, eta_values):
    zeta = np.zeros_like(eta)  # placeholder for external input if needed
    theta = np.array([3, 2, 1, 4, 5])  # example theta values
    result = np.zeros_like(eta)

    for i in range(len(eta)):
        if i < 3:  # For first three eta components (no phase shift)
            result[i] = (gamma[i, i] * xi(t - theta[i]) - eta[i] + zeta[i]) / tau
        else:  # For eta_3 and eta_4 with past eta values
            result[i] = (beta[i, 0] * pastEta(t_values, eta_values, t - theta[i]) + 
                          zeta[i] - eta[i]) / tau

    return result

# Initial conditions
initCond = np.zeros(5)  # Example initial conditions for eta
time = np.linspace(0, 20, 100)  # Time span for the simulation

# Storage for past values
eta_values = []
t_values = []

# Time stepping loop to store past values
for t in time:
    # Calculate current eta
    if len(t_values) == 0 or t > t_values[-1]:  # Only store if it's new time
        eta_current = etaFunc(initCond, t, np.array(t_values), np.array(eta_values))
        eta_values.append(eta_current)
        t_values.append(t)

# Convert lists to arrays for interpolation
eta_values = np.array(eta_values)
t_values = np.array(t_values)

# Final calculation with odeint for the first time
ETA = odeint(etaFunc, initCond, time, args=(t_values, eta_values))

# Example: Accessing individual components of ETA
eta_0 = ETA[:, 0]
eta_1 = ETA[:, 1]
# etc.

print(eta_0)
