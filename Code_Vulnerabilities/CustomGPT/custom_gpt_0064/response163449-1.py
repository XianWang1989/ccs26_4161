
import numpy as np
from scipy.integrate import odeint

# Define the time parameter and time array
time = np.linspace(0, 10, 100)  # From 0 to 10 with 100 points
tau = 3

# Constants
a = 1
b = 5

# Initial conditions
initCond = [0]  # Starting value of Y

def etaFunc(Y, t, history):
    # Create a history of past values
    Y_current = Y[0]

    # Check for the past value based on tau
    if t < tau:
        Y_past = 0  # If time is less than tau, we assume Y(t-tau) is 0
    else:
        Y_past = history[int((t - tau) / (time[1] - time[0]))]

    # Store current Y in history
    history[int(t / (time[1] - time[0]))] = Y_current

    # Return the derivative
    return [a * Y_current + b * Y_past]

# Initialize the history array
history = np.zeros(len(time))

# Integrate using odeint
ETA = odeint(etaFunc, initCond, time, args=(history,))

# Extracting individual components (in this case, just eta_0)
eta_0 = ETA[:, 0]

# Visualization or further processing could happen here
