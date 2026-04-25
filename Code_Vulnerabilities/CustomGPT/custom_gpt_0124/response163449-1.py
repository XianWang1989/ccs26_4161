
import numpy as np
from scipy.integrate import odeint

# Parameters
a = 1
b = 5
tau = 3

# Time parameters
time = np.linspace(0, 20, 100)  # Time points

# Initialization
initCond = [0] * 5  # Initial conditions for eta

# Memory for past values
eta_memory = []  # This will hold past values of eta

def pastEta(t):
    """Retrieve past values of eta at time t."""
    if len(eta_memory) == 0:
        return [0] * 5  # Return zeros if no past values
    # Find the closest past value
    idx = max(0, np.searchsorted(time, t) - 1)
    return eta_memory[idx]

def etaFunc(A, t):
    """Define the differential equations."""
    global eta_memory
    # Save current eta to memory
    eta_memory.append(A.copy())

    # Compute previous eta values for the calculation
    past_values = pastEta(t - tau)

    # Assuming gamma, theta and zeta are defined/initialized elsewhere in your code
    # Here, we mock them for illustration
    gamma = np.eye(5)  # Identity for simplicity in this example
    zeta = np.zeros(5)
    theta = [0] * 5  # Example values for theta

    # Differential equation
    dA_dt = np.array([
        a * A[0] + b * past_values[0],  # Example equation for eta_0
        a * A[1] + b * past_values[1],  # Example equation for eta_1
        a * A[2] + b * past_values[2],  # Example equation for eta_2
        (beta[3, 0] * past_values[3] + beta[3, 1] * past_values[4] - A[3] + zeta[3]) / tau,
        (beta[4, 3] * past_values[3] - A[4] + zeta[4]) / tau
    ])

    return dA_dt

# Dummy beta initialization for demonstration
beta = np.random.rand(5, 5)

# Run the integration
ETA = odeint(etaFunc, initCond, time)

# Now you can access specific components of ETA
eta_0 = ETA[:, 0]
