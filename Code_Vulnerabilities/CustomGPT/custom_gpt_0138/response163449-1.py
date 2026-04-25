
import numpy as np
from scipy.integrate import odeint

# Parameters
a = 1
b = 5
tau = 3

# History to store past values
history = []

def model(Y, t):
    # Store current value in history
    history.append(Y)

    # Ensure history doesn't grow indefinitely
    if len(history) > 1000:  # Keep the last 1000 values
        history.pop(0)

    # Access past value Y(t-tau) based on current time
    if t >= tau:
        past_Y = history[int((t - tau))]  # Integer index for past value
    else:
        past_Y = 0  # No past value available, could be a boundary condition.

    # Differential equation
    dYdt = a * Y + b * past_Y
    return dYdt

# Initial conditions
initCond = [0]  # Adjust as necessary
time = np.linspace(0, 20, 100)  # Total time to simulate

# Solve the ODE
ETA = odeint(model, initCond, time)

# Extract results
eta_0 = ETA[:, 0]

# Example of accessing past values
print("Current ETA:", eta_0)
print("Past values accessible:", history[-10:])  # Last 10 recorded values
