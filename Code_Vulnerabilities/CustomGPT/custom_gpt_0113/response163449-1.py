
import numpy as np
from scipy.integrate import odeint

# Constants
a = 1
b = 5
tau = 3

# Create a buffer for past values
past_values = []

def pastEta(t, t_values, y_values):
    """Get past values of eta based on time."""
    for idx, time in enumerate(t_values):
        if time <= t:
            return y_values[idx]
    return 0  # Return 0 if no past value is found

def etaFunc(A, t, t_values, y_values):
    # Append current time and value to buffers
    past_values.append((t, A))

    # Limit the buffer size to avoid memory overflow
    if len(past_values) > 1000:  # Limiting past values
        past_values.pop(0)

    # Extract past time and values
    past_eta_value = pastEta(t - tau, [p[0] for p in past_values], [p[1] for p in past_values])

    # Differential equation
    dA_dt = a * A + b * past_eta_value
    return dA_dt

# Initial conditions and time points
initCond = 1.0
time = np.linspace(0, 30, 300)

# List to store results
result = []

# Run the ODE solver iteratively to keep track of past values
for t in time:
    result.append(etaFunc(initCond, t, [p[0] for p in past_values], [p[1] for p in past_values]))

ETA = np.array(result)

# Example of accessing individual components
print(ETA)
