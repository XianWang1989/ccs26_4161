
import numpy as np
from scipy.integrate import odeint
from scipy.interpolate import interp1d

# Define constants
a = 1
b = 5
tau = 3  # Phase shift

# Time configuration
time = np.linspace(0, 20, 100)  # Define the time points for integration
initCond = [0] * 5  # Initial conditions for each eta

# To store computed values of eta
eta_values = []

def etaFunc(A, t, past_eta):
    # Interpolate past values
    if len(past_eta) == 0 or t < tau:
        # If there's no past eta or t is too small, return the current state directly
        past_values = [0] * len(A)  # Placeholder for past values
    else:
        # Create an interpolation function
        interp_func = interp1d(time[:len(eta_values)], eta_values, axis=0, fill_value='extrapolate')
        past_values = interp_func(t - tau)

    # Define your system of equations using current and past values of eta
    return np.array([
        a * A[0] + b * past_values[0],
        a * A[1] + b * past_values[1],
        a * A[2] + b * past_values[2],
        (b * past_values[0] - A[3]) / tau,  # Example differential equation
        (b * past_values[1] - A[4]) / tau   # Example differential equation
    ])

# Store the results using odeint
for i in range(len(time)):
    if i == 0:
        # First step, just store the initial condition
        eta_values.append(initCond)
    else:
        # Solve differential equations at each time step
        A_next = odeint(etaFunc, eta_values[-1], [time[i]], args=(eta_values,))
        eta_values.append(A_next[0])

# Convert to numpy array for easier indexing
ETA = np.array(eta_values)

# Access individual components, for example
eta_0 = ETA[:, 0]
eta_1 = ETA[:, 1]
