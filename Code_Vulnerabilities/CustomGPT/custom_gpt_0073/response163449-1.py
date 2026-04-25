
import numpy as np
from scipy.integrate import odeint

# Parameters for the system
a = 1
b = 5
tau = 3

# Initialize storage for past values
past_values = []

def pastEta(t, time, eta):
    # Function to retrieve past estimates based on time shift
    for i, t_val in enumerate(time):
        if t_val <= t:
            return eta[i]
    return 0  # Default if no past value is found

def etaFunc(A, t, time, eta_vals):
    # Calculate the new values based on the current state and past values
    past_eta = pastEta(t - tau, time, eta_vals)
    return np.array([
        a*A[0] + b*A[0],  # Example equation for eta_0
        a*A[1] + b*past_eta # Example equation for eta_1 with phase shift
    ])

# Time settings
time = np.linspace(0, 10, 100)
initCond = [1, 1]  # Initial conditions

# Create a list to store eta values
eta_vals = []

# ODE solver
results = []
A = initCond
for t in time:
    A = odeint(etaFunc, A, [t], args=(time, eta_vals))[0]
    results.append(A)
    eta_vals.append(A)

# Convert results to a NumPy array for easier handling
results = np.array(results)

# Example of accessing individual components
eta_0 = results[:, 0]
eta_1 = results[:, 1]

# Now you can plot or analyze eta_0 and eta_1 as needed
