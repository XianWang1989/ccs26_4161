
import numpy as np
from scipy.integrate import odeint

# Constants
a = 1
b = 5
tau = 3

# Time settings
time = np.linspace(0, 10, 100)  # 0 to 10 seconds, 100 time points

# Initialize storage for `eta`
eta_storage = []

# Define the system of equations with a phase shift
def etaFunc(eta, t):
    global eta_storage

    # Store current value in history
    eta_storage.append(eta.copy())

    # Get previous values if they exist
    past_eta_values = []
    for shift in tau:  # You can customize which indices to reference
        if t - shift >= 0:  # Ensure we reference past times
            # Find the closest previous time point
            idx = np.searchsorted(time, t - shift) - 1
            if idx >= 0:
                past_eta_values.append(eta_storage[idx])
            else:
                past_eta_values.append(0)  # Zero if no past value is available

    # Your differential equation
    d_eta_dt = a * eta + b * sum(past_eta_values) / len(past_eta_values)
    return d_eta_dt

# Initial conditions for eta
init_cond = [0, 0, 0, 0, 0]

# Solve the system of equations
ETA = odeint(etaFunc, init_cond, time)

# Access individual components like eta_0
eta_0 = ETA[:, 0]

# Output the results (for demonstration)
import matplotlib.pyplot as plt

plt.plot(time, eta_0)
plt.title('Solution for eta_0 over time')
plt.xlabel('Time')
plt.ylabel('eta_0')
plt.show()
