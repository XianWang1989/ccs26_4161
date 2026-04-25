
import numpy as np
from scipy.integrate import odeint

# Constants
a = 1.0
b = 5.0
tau = 3.0

# Function to calculate past values of eta
def pastEta(t, history, time_points):
    # Return the last available value before time t
    for i in range(len(time_points)-1, -1, -1):
        if time_points[i] <= t:
            return history[i]
    return 0  # returns 0 if no past value is found

# Differential equations system
def etaFunc(A, t, history, time_points):
    # Update history
    history.append(A.copy())
    # Ensure we only keep the last tau steps in history
    if len(history) > (tau+1):  # tau + 1 to include current time
        history.pop(0)

    # Calculate past value
    Y_tau = pastEta(t - tau, history, time_points)
    return np.array([a * A[0] + b * Y_tau])

# Time points for integration
time = np.linspace(0, 30, 100)  # 0 to 30 seconds
initCond = [0.0]  # Initial condition

# History to store past values
history = []
time_points = []  # Corresponding time points for the history

# Apply odeint
ETA = np.zeros((len(time), len(initCond)))  # Preallocation for output
for i, t_val in enumerate(time):
    time_points.append(t_val)
    ETA[i] = odeint(etaFunc, initCond, [t_val], args=(history, time_points))[-1]

# You can extract individual components like this:
eta_0 = ETA[:, 0]
