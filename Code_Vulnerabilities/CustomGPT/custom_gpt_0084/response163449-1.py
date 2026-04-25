
import numpy as np
from scipy.integrate import odeint

# Constants
a = 1
b = 5
tau = 3

# Define the function to get past values
def get_past_values(t_current, t_past, eta_history):
    # Ensure the request time is valid
    if t_past < 0 or t_past >= t_current:
        return 0  # Or handle it according to your needs
    # Find the closest past index
    index = int(t_past)  # Assuming t is an integer time
    return eta_history[index] if index < len(eta_history) else 0

# Define the system of equations
def etaFunc(eta, t, eta_history):
    # Store the current eta for future usage
    eta_history.append(eta.copy())

    # Compute values needed for the equations
    y_3 = get_past_values(t, t - tau, eta_history)

    # Return the derivatives
    return np.array([
        a * eta[0] + b * y_3,
        # Add additional equations as needed
    ])

# Time settings
time = np.linspace(0, 10, 100)  # from t=0 to t=10
initCond = [0.1]  # Initial conditions
eta_history = []  # List to store past values

# Integrate the ODEs
ETA = odeint(etaFunc, initCond, time, args=(eta_history,))

# Extract individual components
eta_0 = ETA[:, 0]

# For debugging, you can print or plot results
print(eta_0)
