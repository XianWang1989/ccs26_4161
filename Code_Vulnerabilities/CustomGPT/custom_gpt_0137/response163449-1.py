
import numpy as np
from scipy.integrate import odeint

# Parameters
a = 1
b = 5
tau = 3
theta = [1, 2, 3, 4, 5]  # Some phase shift constants

# Function to calculate eta. This can be your more complex version.
def etaFunc(A, t, past_values):
    # Use past_values list to retrieve past eta values based on t and theta
    Y = np.zeros_like(A)

    # Assuming A has 5 components (eta_0 to eta_4)
    for i in range(len(A)):
        if t - theta[i] >= 0:  # Only consider past values
            lag_index = int(t - theta[i])
            if lag_index < len(past_values):  # Check bounds
                Y[i] = a * A[i] + b * past_values[lag_index]  # This takes Y(t-tau) 
            else:
                Y[i] = a * A[i]  # Default to just the current if no past value
        else:
            Y[i] = a * A[i]  # Default if phase shift is not applicable

    return Y

# Integration function
def integrate_system(initCond, time):
    n = len(initCond)
    past_values = []

    # Wrapper to include past values
    def wrapper(A, t):
        past_values.append(A)  # Store current A for future calls
        return etaFunc(A, t, past_values)

    # Run integration
    ETA = odeint(wrapper, initCond, time)

    return ETA

# Initial conditions and time
initCond = [0, 0, 0, 0, 0]  # Example initial values for eta_0 to eta_4
time = np.linspace(0, 10, 100)  # Time from 0 to 10 seconds

ETA = integrate_system(initCond, time)

# Example output
print(ETA[:, 0])  # Accessing the first component, eta_0
