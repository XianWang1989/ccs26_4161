
import numpy as np
from scipy.integrate import odeint

# Define constants
a = 1
b = 5
tau = 3

# History buffer for past_eta values
history = []

# Define the function to return past eta values
def past_eta(t_val, time, eta_values):
    indices = np.where(time < t_val)[0]
    if len(indices) == 0:
        return [0] * len(eta_values[0])  # Return zeros if no past values
    return eta_values[indices[-1]]  # Return the most recent past values

# Define the system of equations
def eta_func(A, t, time, eta_history):
    history.append(A)  # Store current value
    if len(time) < len(history):
        time.append(t)  # Keep track of time

    # Assuming theta values are constant here
    theta = [1, 2, 3, 4]  # Example theta values
    eta_past = past_eta(t - tau, time, history)

    # Define the derivatives
    dA_dt = np.array([
        a * A[0] + b * eta_past[0],
        a * A[1] + b * eta_past[1],
        a * A[2] + b * eta_past[2],
        a * A[3] + b * eta_past[3],
        a * A[4] + b * eta_past[4]
    ])
    return dA_dt

# Initial conditions
init_cond = [0, 0, 0, 0, 0]
time = []

# Time points where we want the solution
t_points = np.linspace(0, 20, 100)

# Run the integration
ETA = odeint(eta_func, init_cond, t_points, args=(time, history))

# Access individual components
eta_0 = ETA[:, 0]
eta_1 = ETA[:, 1]
eta_2 = ETA[:, 2]
eta_3 = ETA[:, 3]
eta_4 = ETA[:, 4]
