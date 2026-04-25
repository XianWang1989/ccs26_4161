
import numpy as np
from scipy.integrate import odeint
from scipy.interpolate import interp1d

# Constants
a = 1
b = 5
tau = 3

# Time parameters
time = np.linspace(0, 20, 100)  # Time points for the integration

# Initial conditions
initCond = [0, 0, 0, 0, 0]  # Example initial values for eta

# Function to define your differential equations
def etaFunc(eta, t, past_eta_func):
    # Retrieve past values using the provided interpolation function
    past_eta_3 = past_eta_func(t - tau) if t - tau >= 0 else 0

    # Define your system of equations
    d_eta_dt = np.array([
        a * eta[0] + b * eta[0],  # Example derivative for eta[0]
        a * eta[1] + b * eta[1],  # Example derivative for eta[1]
        a * eta[2] + b * eta[2],  # Example derivative for eta[2]
        a * eta[3] + b * past_eta_3,  # Example, influenced by past_eta_3
        a * eta[4]                 # Example derivative for eta[4]
    ])

    return d_eta_dt

# Store the results for interpolation
initial_results = np.array([initCond])  # Store initial results for interpolation

# Performing integration
ETA = odeint(etaFunc, initCond, time)

# Create interpolation function for past eta values
past_eta_func = interp1d(time, ETA, axis=0, bounds_error=False, fill_value=0)

# Example of retrieving results
eta_0 = ETA[:, 0]
# You can now also get eta_3 and eta_4 using similar indexing, e.g. ETA[:, 3]

# Optional: Plot your results
import matplotlib.pyplot as plt

plt.plot(time, eta_0, label='eta_0')
plt.xlabel('Time')
plt.ylabel('Values of eta_0')
plt.legend()
plt.show()
