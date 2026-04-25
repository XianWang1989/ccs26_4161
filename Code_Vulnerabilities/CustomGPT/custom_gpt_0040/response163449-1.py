
import numpy as np
from scipy.integrate import odeint

# Parameters
a = 1
b = 5
tau = 3  # Phase shift

# Time settings
time = np.linspace(0, 20, 200)  # Time array

def eqtnSystem(Y, t, past_Y):
    # Unpack Y
    Y_current = Y[0]

    # Get past value based on phase shift
    Y_past = past_Y.get(t-tau, 0)  # Default to 0 if no past value

    # The differential equation
    dYdt = a * Y_current + b * Y_past
    return [dYdt]

# Initialize conditions
initCond = [1]  # Initial condition
Y_history = {}  # Dictionary to store past values

# Container for results
results = []

for t in time:
    # Integrate with respect to the current time t
    Y = eqtnSystem(initCond, t, Y_history)

    # Store the current solution
    results.append(Y[0])

    # Update the historical values for the next iteration
    Y_history[t] = Y[0]

# Convert results to numpy array
ETA = np.array(results)

# Example of extracting individual components
eta_0 = ETA  # Since we only have one component in this example

print(eta_0)
