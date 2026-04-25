
import numpy as np
from scipy.integrate import odeint

# A global list to store past values of Y
past_values = []

def eqtnSystem(Y, t, a=1, b=5, tau=3):
    # Ensure we have past values for the time-shift
    if len(past_values) < tau: 
        past_values.append(Y)  # Fill past values initially

    # Shifted value (Y(t-tau))
    if t >= tau:
        Y_tau = past_values[-tau]  # Get value from tau time steps ago
    else:
        Y_tau = 0  # Default if not enough past values

    # Store the current value in past_values
    past_values.append(Y)

    # Return the derivative
    return a * Y + b * Y_tau

# Time points
time = np.linspace(0, 10, 100)

# Initial condition
initCond = [0]

# Solve ODE
ETA = odeint(eqtnSystem, initCond, time)

# Extract individual components
eta_0 = ETA[:, 0]

# Print results for verification
print(eta_0)
