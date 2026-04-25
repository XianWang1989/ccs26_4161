
import numpy as np
from scipy.integrate import odeint

# Constants
a = 1
b = 5
tau = 3  # time delay

# Define the differential equation system
def eqtnSystem(Y, t, past_values):
    current_val = Y[0]

    # Access the past value at t - tau using interpolation
    if t - tau < 0:
        past_val = 0  # Start value if before 0
    else:
        # Ensure we get the past value corresponding to t - tau
        idx = int(t - tau)
        past_val = past_values[idx] if idx < len(past_values) else 0

    return [a * current_val + b * past_val]

# Time settings
time = np.linspace(0, 20, 100)
init_cond = [1]  # initial value

# Create an array to store past values
past_values = np.zeros(len(time))

# Perform integration
for i, t_val in enumerate(time):
    if i == 0:
        past_values[i] = init_cond[0]  # Store initial condition
        continue

    # Integrate step using the system defined
    result = odeint(eqtnSystem, [past_values[i-1]], [time[i], time[i]])
    past_values[i] = result[-1, 0]  # Update past values

# You can now access the results through past_values array
print(past_values)
