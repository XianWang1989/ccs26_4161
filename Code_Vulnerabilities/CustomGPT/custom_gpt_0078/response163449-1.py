
import numpy as np
from scipy.integrate import odeint

# Constants (you can define these based on your model)
a = 1.0
b = 5.0
tau = 3.0
theta = [1, 2, 3, 4, 5, 6, 7]
beta = np.random.rand(5, 5)  # Replace with your actual beta
gamma = np.random.rand(5, 5)  # Replace with your actual gamma
zeta = np.random.rand(5)      # Replace with your actual zeta

# Function to compute past eta values
def pastEta(t, history, index):
    if t < 0:
        return 0
    for time, values in reversed(history):
        if time <= t:
            return values[index]
    return 0

# Main function for ODE system
def etaFunc(A, t, history):
    # Store current values for history
    history.append((t, A.copy()))

    results = np.zeros_like(A)

    results[0] = a * A[0] + b * pastEta(t - tau, history, 0)
    results[1] = a * A[1] + b * pastEta(t - tau, history, 1)
    # Add more equations as needed...

    return results

# Time vector for simulation
time = np.linspace(0, 10, 100)
initCond = np.zeros(5)  # Initial conditions for eta values

# Store history for past values
history = []

# Run the ODE solver
ETA = odeint(lambda A, t: etaFunc(A, t, history), initCond, time)

# Example of retrieving components
eta_0 = ETA[:, 0]
# And so on for eta_1, eta_2, etc.

print(eta_0)
