
import numpy as np
from scipy.integrate import odeint

# Parameters
a = 1
b = 5
tau = 3

# Initialize past values array
past_values = []

def past_eta(t, history, tau):
    """ Retrieve value of Y at time t - tau if within history bounds. """
    if t - tau < 0:
        return 0  # Return zero or some initial condition if out of bounds
    for time, value in reversed(history):
        if time <= t - tau:
            return value
    return 0  # Fallback if no suitable past value found

def eqtn_system(Y, t, history):
    """ Define the equations for the ODE system. """
    Y_current = Y[0]
    Y_past = past_eta(t, history, tau)

    dYdt = a * Y_current + b * Y_past
    return [dYdt]

# Time settings
time = np.linspace(0, 10, 100)  # Time span for the ODE solver
init_cond = [1]  # Initial condition for Y

# Container for results
results = []

def store_results(t, Y, history):
    """ Store the current state in the history for reference. """
    history.append((t, Y[0]))  # Append current time and Y value

# ODE integration
for t in time:
    if len(results) > 0:
        current_Y = results[-1]
    else:
        current_Y = init_cond

    # Create a new state for the current time
    new_Y = odeint(eqtn_system, current_Y, [t], args=(past_values,))
    results.append(new_Y[0])

    # Store the result for future retrieval
    store_results(t, new_Y[0], past_values)

# Convert results to a numpy array for analysis
ETA = np.array(results)

# Example output
print("ETA:", ETA[:,0])
