
import numpy as np
from scipy.integrate import odeint

# Constants for your equations
a = 1
b = 5
tau = 3  # Delay in the system

# Number of components
num_components = 5

# Initialize an array to store past values
past_eta = np.zeros((num_components, 1000))  # Assuming a maximum of 1000 time steps
time_steps = np.linspace(0, 10, 1000)  # Example time array
initCond = np.ones(num_components)  # Initial conditions

# Function to fetch past values; ensure correct bounds
def get_past_eta(t, theta, current_time_idx):
    past_vals = []
    for shift in theta:
        idx = current_time_idx - int(shift / (time_steps[1] - time_steps[0]))
        if idx >= 0:
            past_vals.append(past_eta[:, idx])
        else:
            past_vals.append(np.zeros(num_components))  # or handle as needed
    return np.array(past_vals)

# Main function that defines the system of equations
def etaFunc(A, t, current_time_idx, theta):
    global past_eta
    Y = A
    # Get past values based on shifted time
    past_vals = get_past_eta(t, theta, current_time_idx)

    # Define your differential equations
    dYdt = np.zeros(num_components)
    dYdt[0] = a * Y[0] + b * past_vals[0][0]  # Example using past values for 0th component
    # Repeat for other components as needed...

    return dYdt

theta = [3, 4, 5]  # Example phase shifts corresponding to past delayed inputs
ETA = np.zeros((len(time_steps), num_components))  # To store results

# Loop over each time step to calculate the solution manually
for i, t in enumerate(time_steps):
    if i == 0:
        ETA[i] = initCond
    else:
        ETA[i] = odeint(etaFunc, ETA[i-1], [time_steps[i-1], time_steps[i]], args=(i, theta))[-1]

# Now you can access any particular component, such as:
eta_0 = ETA[:, 0]
