
import numpy as np
from scipy.integrate import odeint

# Parameters
a = 1.0
b = 5.0
tau = 3.0

# Time parameters
start_time = 0
end_time = 25
time = np.linspace(start_time, end_time, 100)

# Initial conditions
initCond = [0]  # Initial value of Y at t=0

# This will keep track of past values of Y
def past_values(t, history):
    # This function retrieves the appropriate past value from history
    # Check if t-tau is within the bounds of the tracked history
    idx = np.searchsorted(time, t - tau)  # Find index of t-tau in the time array
    if idx > 0:
        return history[idx - 1]  # The value at t-tau is the last stored value before t-tau
    else:
        return 0  # Return 0 or any default if t-tau is out of bounds

def eqtnSystem(Y, t, history):
    # Use previous history to calculate Y(t-tau)
    Y_tau = past_values(t, history)
    dYdt = a * Y + b * Y_tau
    return dYdt

# Store the history for past values of Y
def integrate_system(initCond, time):
    history = [initCond[0]]  # Start with initial condition
    results = []

    for t in time:
        if len(results) > 0:
            current_Y = results[-1]  # Get last calculated value of Y
        else:
            current_Y = initCond[0]  # If first step, use initial condition

        # Calculate the derivative
        dYdt = eqtnSystem(current_Y, t, history)

        # Update the value of Y with a simple Euler step (could use odeint, but keeping it simple here)
        new_Y = current_Y + dYdt * (time[1] - time[0])  # Time step size
        results.append(new_Y)
        history.append(new_Y)  # Append the latest value to history

    return np.array(results)

# Perform the integration
ETA = integrate_system(initCond, time)

# Access individual components of ETA
print(ETA)
