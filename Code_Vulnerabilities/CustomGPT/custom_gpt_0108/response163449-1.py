
import numpy as np
from scipy.integrate import odeint

# Global storage for past values
past_values = []

def pastEta(t):
    # Returns the last known eta value before time t
    if past_values and t > 0:
        return past_values[int(t)]
    else:
        return 0.0  # or any initial value

def etaFunc(A, t):
    global past_values  # To access the global past_values
    # Store the current value of A in past_values if valid timestamp
    if t >= len(past_values):
        past_values.append(A.copy())

    # Define constants
    gamma = np.array([[1]])  # Example, replace with actual values
    zeta = np.array([0])  # Example
    tau = np.array([3])  # Example
    theta = np.array([1])  # Example

    # Use pastEta to retrieve values for calculations
    eta_values = [
        (gamma[0, 0] * xi(t - theta[0])[0] - A[0] + zeta[0]) / tau[0],
        # Repeat for other elements...
        (beta[3, 0] * pastEta(t - theta[3]) + beta[3, 1] * pastEta(t - theta[4]) - A[3] + zeta[3]) / tau[3],
        # Additional terms...
    ]

    return np.array(eta_values)

# xi and beta need to be defined according to your model
def xi(t):
    return np.array([np.sin(t), np.cos(t)])  # Example implementation

# Set initial conditions and time vector
initCond = np.zeros(5)  # Adjust based on the number of equations you have
time = np.linspace(0, 10, 100)  # Time array

# Call odeint
ETA = odeint(etaFunc, initCond, time)

# Access results
eta_0 = ETA[:, 0]
