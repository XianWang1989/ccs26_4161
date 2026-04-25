
import numpy as np
from scipy.integrate import odeint

# Parameters
a = 1
b = 5
tau = 3

# Initialize storage for past values
past_values = []

def eqtnSystem(Y, t):
    global past_values
    current_Y = Y[0]

    # Retrieve past value if it exists
    if len(past_values) >= 1:
        delayed_Y = past_values[-1]  # Y(t - tau)
    else:
        delayed_Y = 0  # Handle the case when no past value exists

    # Update past values with the current value
    past_values.append(current_Y)

    # Keep only the last tau values to avoid memory issues
    if len(past_values) > tau:
        past_values.pop(0)

    # Differential equation
    dYdt = a * current_Y + b * delayed_Y
    return [dYdt]

# Initial condition
initCond = [0]
time = np.linspace(0, 20, 100)

# Integration
ETA = odeint(eqtnSystem, initCond, time)

# Retrieve specific components
eta_0 = ETA[:, 0]

# Example plot (optional)
import matplotlib.pyplot as plt
plt.plot(time, eta_0)
plt.xlabel('Time')
plt.ylabel('ETA')
plt.title('Solution of the Differential Equation with Phase Shift')
plt.show()
