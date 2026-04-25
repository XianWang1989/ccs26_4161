
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Define the parameters
a = 1
b = 5
tau = 3
theta = [0, 0, 0, tau, 2*tau]  # Example values for theta

# History array to store the values of eta over time
history = []

# Function to retrieve past values based on time shift
def pastEta(t, time_array, eta_array, shift):
    index = np.searchsorted(time_array, t - shift) - 1
    if index >= 0:
        return eta_array[index]
    else:
        return 0  # If no past value is available, return 0 or use an alternative

# System of equations with time shifts
def etaFunc(eta, t, time_array):
    # Append current eta state to history
    history.append(eta)

    # Ensure history is not longer than needed
    if len(history) > len(time_array):
        history.pop(0)

    # Retrieve past values based on theta shifts
    past_eta3 = pastEta(t, time_array, history, tau)
    past_eta4 = pastEta(t, time_array, history, 2 * tau)

    return np.array([
        a*eta[0] + b*past_eta3,
        a*eta[1] + b*past_eta4,
        a*eta[2]  # Assuming no past for eta[2] in this example
    ])

# Time array for integration
time = np.linspace(0, 30, 100)  # From 0 to 30 seconds
initCond = [0, 0, 0]  # Initial conditions for eta

# Store results
ETA = odeint(etaFunc, initCond, time, args=(time,))

# Plotting results
plt.figure(figsize=(10, 6))
plt.plot(time, ETA[:, 0], label='eta_0')
plt.plot(time, ETA[:, 1], label='eta_1')
plt.plot(time, ETA[:, 2], label='eta_2')
plt.xlabel('Time')
plt.ylabel('Values of eta')
plt.legend()
plt.title('Differential Equations with Phase Shift')
plt.grid()
plt.show()
