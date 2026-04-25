
import numpy as np
from scipy.integrate import odeint

# Define parameters
a = 1
b = 5
tau = 3  # Time delay

# Define the system with phase shift
def eqtnSystem(Y, t, past_values):
    if t < tau:
        return [0]  # Handle initial condition if needed

    # Retrieve past value based on time delay
    past_index = int(t - tau)
    if past_index >= 0:
        Y_past = past_values[past_index]  # Get past value (Y(t-tau))
    else:
        Y_past = 0  # Handle edge case

    return [a * Y[0] + b * Y_past]

# Initialization
time_points = np.linspace(0, 10, 100)  # Time points for integration
init_cond = [1]  # Initial condition
past_values = [0] * len(time_points)  # Storage for past values

# Store results to compute past values
results = []
for i, t in enumerate(time_points):
    if i > 0:
        # Get the previous result
        past_values[i - 1] = results[-1][0] if results else init_cond[0]

    # Integrate the equation
    sol = odeint(eqtnSystem, init_cond, [t], args=(past_values,))
    results.append(sol[-1])  # Store the latest result

# Convert results to numpy array for easier indexing
results = np.array(results)

# Output values
eta_0 = results[:, 0]
