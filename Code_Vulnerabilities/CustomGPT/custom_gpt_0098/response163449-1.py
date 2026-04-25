
import numpy as np
from scipy.integrate import odeint

# Parameters
a = 1
b = 5
tau = 3

# Function to calculate past values
def pastEta(t, theta, ETA, time):
    # Identify indices for past values
    past_indices = [np.searchsorted(time, t - theta_i) for theta_i in theta if t - theta_i >= 0]

    # Return the past values, ensuring we stay within bounds
    return [ETA[i] for i in past_indices if i < len(ETA)]

# Differential equation system
def etaFunc(A, t, theta):
    zeta = np.zeros_like(A)  # Replace with your zeta calculation
    past_etaa = pastEta(t, theta, ETA, time)

    # Example derivative function for eta
    dYdt = np.zeros_like(A)
    dYdt[0] = a * A[0] + b * (past_etaa[0] if past_etaa else 0) / tau

    # Add calculations for other elements in A as needed
    # ... (similar equations for dYdt[1], dYdt[2], ...)

    return dYdt

# Initial conditions and time
initCond = np.zeros(5)  # Number of equations (5 in this case)
time = np.linspace(0, 10, 100)  # Define time array
theta = [1, 2, 3]  # Example phase shifts

# Integrate
ETA = odeint(etaFunc, initCond, time, args=(theta,))

# Access components of ETA
eta_0 = ETA[:, 0]
eta_1 = ETA[:, 1]
# ... and so on
