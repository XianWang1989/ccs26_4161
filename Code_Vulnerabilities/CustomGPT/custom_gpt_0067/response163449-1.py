
import numpy as np
from scipy.integrate import odeint

# Define constants
a = 1
b = 5
tau = 3

# Initialize an array to store past values
past_eta = []

def interpolate_past(t, t_values, eta_values):
    # Simple linear interpolation for past values
    if t <= t_values[0]:
        return eta_values[0]

    for i in range(1, len(t_values)):
        if t_values[i] > t:
            return np.interp(t, t_values[i-1:i+1], eta_values[i-1:i+1])

    return eta_values[-1]

def etaFunc(y, t, t_values, eta_values):
    # Retrieve past eta using interpolation
    past_value = interpolate_past(t - tau, t_values, eta_values)

    # Current differential equation
    dydt = a * y + b * past_value
    return dydt

# Time points
time = np.linspace(0, 20, 100)
initCond = [0]  # Initial condition
eta_values = [initCond[0]]  # Store initial eta value
t_values = [time[0]]  # Store the corresponding time points

# Compute the solution
ETA = []
for t in time:
    current_eta = odeint(etaFunc, initCond, [t], args=(t_values, eta_values))
    ETA.append(current_eta[0][0])

    # Update past values
    past_eta.append(current_eta[0][0])
    t_values.append(t)

# Convert ETA to array for further use
ETA = np.array(ETA)

# Access individual components
eta_0 = ETA[:, 0]

# Optionally print or plot results
print(eta_0)
