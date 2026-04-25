
import numpy as np
from scipy.integrate import odeint

# Constants
a = 1
b = 5
tau = 3

# Function to calculate the past values using interpolation
def past_values(t, eta, time):
    # Check if t-tau is in the time array
    if t - tau < time[0]:
        return 0  # Return a default value if we're out of bounds
    else:
        # Interpolate to get the previous value of eta
        return np.interp(t - tau, time, eta)

# Define the system of equations
def eqtn_system(A, t, time, eta):
    Y = A
    # Get the past value using the defined function
    past_Y = past_values(t, eta, time)
    return a * Y + b * past_Y

# Time setup
time = np.linspace(0, 20, 100)
initCond = [1]  # Initial condition

# Store results
results = np.zeros((len(time), len(initCond)))
results[0] = initCond

# Integration loop
for i in range(1, len(time)):
    t_current = time[i]
    # Call the ODE system and store the result
    results[i] = odeint(eqtn_system, results[i-1], [time[i-1], time[i]], args=(time, results[:, 0]))[-1]

# Extract components
eta = results[:, 0]

# Plotting the results
import matplotlib.pyplot as plt

plt.plot(time, eta)
plt.xlabel('Time')
plt.ylabel('Eta')
plt.title('Phase-shifted ODE Solution')
plt.show()
